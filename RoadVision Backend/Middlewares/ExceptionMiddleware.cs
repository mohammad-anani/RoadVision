using Microsoft.EntityFrameworkCore;
using System.Text.Json;

namespace RoadVision_Backend.Middlewares
{
    public class ExceptionMiddleware
    {
        private readonly RequestDelegate _next;
        private readonly ILogger<ExceptionMiddleware> _logger;

        public ExceptionMiddleware(
            RequestDelegate next,
            ILogger<ExceptionMiddleware> logger)
        {
            _next = next;
            _logger = logger;
        }

        public async Task Invoke(HttpContext context)
        {
            try
            {
                await _next(context);
            }
            catch (Exception ex)
            {
                _logger.LogError(
                    ex,
                    "Unhandled exception occurred. RequestId: {RequestId}",
                    context.TraceIdentifier);

                if (context.Response.HasStarted)
                    throw;

                await HandleExceptionAsync(context, ex);
            }
        }

        private async Task HandleExceptionAsync(
            HttpContext context,
            Exception exception)
        {
            context.Response.ContentType = "application/json";

            var (statusCode, message) = exception switch
            {
                NotImplementedException =>
                    (StatusCodes.Status501NotImplemented,
                     "This functionality is not implemented yet"),

                KeyNotFoundException =>
                    (StatusCodes.Status404NotFound,
                     "Resource not found"),

                UnauthorizedAccessException =>
                    (StatusCodes.Status401Unauthorized,
                     "Unauthorized access"),

                ArgumentNullException =>
                    (StatusCodes.Status400BadRequest,
                     "Required value is missing"),

                ArgumentOutOfRangeException =>
                    (StatusCodes.Status400BadRequest,
                     "Value is out of range"),

                ArgumentException =>
                    (StatusCodes.Status400BadRequest,
                     "Invalid argument"),

                InvalidOperationException =>
                    (StatusCodes.Status400BadRequest,
                     exception.Message),

                FormatException =>
                    (StatusCodes.Status400BadRequest,
                     "Invalid format"),

                JsonException =>
                    (StatusCodes.Status400BadRequest,
                     "Invalid JSON format"),

                DbUpdateException =>
                    (StatusCodes.Status500InternalServerError,
                     "Database operation failed"),

                TimeoutException =>
                    (StatusCodes.Status408RequestTimeout,
                     "Request timed out"),

                OperationCanceledException =>
                    (499,
                     "Request cancelled"),

                _ =>
                    (StatusCodes.Status500InternalServerError,
                     "An unexpected error occurred")
            };

            context.Response.StatusCode = statusCode;

            await context.Response.WriteAsJsonAsync(new
            {
                error = message,
                requestId = context.TraceIdentifier
            });
        }
    }
}