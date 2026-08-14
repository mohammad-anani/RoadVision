using Microsoft.EntityFrameworkCore;

namespace RoadVision_Backend.Data.DbContextStore
{
    public partial class RoadVisionDbContext : DbContext
    {
        public RoadVisionDbContext()
        {
        }

        public RoadVisionDbContext(DbContextOptions<RoadVisionDbContext> options)
            : base(options)
        {
        }

        public virtual DbSet<DetectedCar> DetectedCars { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<DetectedCar>(entity =>
            {
                entity.ToTable("DetectedCars", tb =>
                {
                    tb.HasCheckConstraint(
                        "CK_DetectedCars_CarInfoGroup",
                        "([CarInfo] IS NULL AND [CarInfoConfidence] IS NULL) OR ([CarInfo] IS NOT NULL AND [CarInfoConfidence] IS NOT NULL)");

                    tb.HasCheckConstraint(
                        "CK_DetectedCars_PlateNumberGroup",
                        "([PlateNumber] IS NULL AND [PlateNumberConfidence] IS NULL) OR ([PlateNumber] IS NOT NULL AND [PlateNumberConfidence] IS NOT NULL)");

                    tb.HasCheckConstraint(
                        "CK_DetectedCars_AtLeastOneGroupRequired",
                        "[CarInfo] IS NOT NULL OR [PlateNumber] IS NOT NULL");

                    tb.HasCheckConstraint(
                        "CK_DetectedCars_CarInfoConfidenceRange",
                        "[CarInfoConfidence] BETWEEN 0.00 AND 1.00");

                    tb.HasCheckConstraint(
                        "CK_DetectedCars_PlateNumberConfidenceRange",
                        "[PlateNumberConfidence] BETWEEN 0.00 AND 1.00");
                });

                entity.HasKey(e => e.Id);

                entity.Property(e => e.Id)
                    .ValueGeneratedOnAdd();

                entity.Property(e => e.DetectedAt)
                    .IsRequired()
                    .HasColumnType("datetime");

                entity.Property(e => e.CarInfo)
                    .HasMaxLength(200)
                    .IsUnicode(true);

                entity.Property(e => e.CarInfoConfidence)
                    .HasColumnType("decimal(3,2)");

                entity.Property(e => e.PlateNumber)
                    .HasMaxLength(200)
                    .IsUnicode(true);

                entity.Property(e => e.PlateNumberConfidence)
                    .HasColumnType("decimal(3,2)");

                entity.Property(e => e.ImagePath)
                    .IsRequired()
                    .IsUnicode(true)
                    .HasColumnType("nvarchar(max)");
            });
        }
    }
}