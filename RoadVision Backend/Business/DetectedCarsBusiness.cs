using RoadVision_Backend.Data;
using RoadVision_Backend.Data.DbContextStore;

namespace RoadVision_Backend.Business
{
    public class DetectedCarsBusiness
    {
        private readonly DetectedCarsData _detectedCarsData;

        public DetectedCarsBusiness(DetectedCarsData detectedCarsData)
        {
            _detectedCarsData = detectedCarsData;
        }

        public async Task<DetectedCar> AddDetectedCarAsync(
            DetectedCar detectedCar,
            IFormFile image)
        {
            detectedCar.Id = 0;

            string imagePath = await SaveImageAsync(image);

            detectedCar.ImagePath = imagePath;

            return await _detectedCarsData.InsertAsync(detectedCar);
        }

        public async Task<List<DetectedCar>> GetAllDetectedCarsAsync()
        {
            return await _detectedCarsData.GetAllAsync();
        }

        public async Task<string> SaveImageAsync(IFormFile image)
        {
            if (image == null || image.Length == 0)
                throw new ArgumentException("Image is required.");

            var imagesFolder = Path.Combine(
                Directory.GetCurrentDirectory(),
                "wwwroot",
                "images",
                "detected-cars"
            );

            Directory.CreateDirectory(imagesFolder);

            var extension = Path.GetExtension(image.FileName);

            if (string.IsNullOrEmpty(extension))
                extension = ".jpg";

            var fileName = $"{Guid.NewGuid()}{extension}";

            var filePath = Path.Combine(imagesFolder, fileName);

            await using var stream = new FileStream(
                filePath,
                FileMode.Create
            );

            await image.CopyToAsync(stream);

            // Path that can be stored in the database
            return $"/images/detected-cars/{fileName}";
        }
    }
}