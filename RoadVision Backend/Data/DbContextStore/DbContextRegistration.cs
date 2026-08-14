using Microsoft.EntityFrameworkCore;

namespace RoadVision_Backend.Data.DbContextStore
{
    public static class DbContextRegistration
    {
        public static IServiceCollection AddDbContext(this IServiceCollection services, IConfiguration configuration)
        {
            // The connection string is retrieved from the appsettings.json file
            string? connectionString = configuration.GetConnectionString("DefaultConnection");

            //Register DbContext with SQL Server and enable logging of SQL queries
            services.AddDbContext<RoadVisionDbContext>(options =>
                options.UseSqlServer(
                    connectionString
                ).LogTo(Console.WriteLine, LogLevel.Information));

            return services;
        }
    }
}