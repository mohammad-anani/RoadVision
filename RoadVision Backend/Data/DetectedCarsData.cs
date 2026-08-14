using Microsoft.EntityFrameworkCore;
using RoadVision_Backend.Data.DbContextStore;

namespace RoadVision_Backend.Data
{
    public class DetectedCarsData
    {
        private readonly RoadVisionDbContext _context;

        public DetectedCarsData(RoadVisionDbContext context)
        {
            _context = context;
        }

        public async Task<DetectedCar> InsertAsync(DetectedCar detectedCar)
        {
            _context.DetectedCars.Add(detectedCar);
            await _context.SaveChangesAsync();
            return detectedCar;
        }

        public async Task<List<DetectedCar>> InsertManyAsync(List<DetectedCar> detectedCars)
        {
            var carsList = detectedCars.ToList();

            if (carsList.Count == 0)
                return carsList;

            _context.DetectedCars.AddRange(carsList);
            await _context.SaveChangesAsync();
            return carsList;
        }

        public async Task<List<DetectedCar>> GetAllAsync()
        {
            return await _context.DetectedCars
                .AsNoTracking()
                .OrderByDescending(d => d.DetectedAt)
                .ToListAsync();
        }
    }
}