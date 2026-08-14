using Microsoft.EntityFrameworkCore;
using RoadVision_Backend.Business;
using RoadVision_Backend.Data;
using RoadVision_Backend.Data.DbContextStore;
using RoadVision_Backend.Middlewares;
using Serilog;

var builder = WebApplication.CreateBuilder(args);

// ======================================================
// Serilog
// ======================================================

Log.Logger = new LoggerConfiguration()
    .ReadFrom.Configuration(builder.Configuration)
    .Enrich.FromLogContext()
    .WriteTo.Console(
        outputTemplate:
        "[{Timestamp:HH:mm:ss} {Level:u3}] " +
        "{Message:lj}{NewLine}{Exception}")
    .CreateLogger();

builder.Host.UseSerilog();

// ======================================================
// Database
// ======================================================

var connectionString =
    builder.Configuration.GetConnectionString("DefaultConnection");

builder.Services.AddDbContext<RoadVisionDbContext>(options =>
{
    options.UseSqlServer(connectionString);

    // Show EF Core SQL queries in the console
    options.LogTo(Console.WriteLine, LogLevel.Information);
});

// ======================================================
// Business / Data Services
// ======================================================

builder.Services.AddScoped<DetectedCarsData>();
builder.Services.AddScoped<DetectedCarsBusiness>();

// ======================================================
// Controllers
// ======================================================

builder.Services.AddControllers();

// ======================================================
// Swagger
// ======================================================

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// ======================================================
//  CORS
// ======================================================

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy
            .AllowAnyOrigin()
            .AllowAnyMethod()
            .AllowAnyHeader();
    });
});

// ======================================================
// Build application
// ======================================================

var app = builder.Build();

// ======================================================
// Middleware
// ======================================================

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();

    app.UseSwaggerUI();
}

app.UseStaticFiles();

app.UseCors("AllowAll");

app.UseHttpsRedirection();

app.UseSerilogRequestLogging();

app.UseMiddleware<ExceptionMiddleware>();

app.UseAuthorization();

// ======================================================
// Controllers / Endpoints
// ======================================================

app.MapControllers();

app.Run();