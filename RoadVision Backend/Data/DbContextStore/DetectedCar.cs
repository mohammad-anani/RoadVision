namespace RoadVision_Backend.Data.DbContextStore
{
    public class DetectedCar
    {
        public int Id { get; set; }
        public DateTime DetectedAt { get; set; }

        public string? CarInfo { get; set; }
        public decimal? CarInfoConfidence { get; set; }

        public string? PlateNumber { get; set; }
        public decimal? PlateNumberConfidence { get; set; }

        public string? ImagePath { get; set; } = null!;
    }
}