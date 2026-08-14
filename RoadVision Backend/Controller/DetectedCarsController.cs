using Microsoft.AspNetCore.Mvc;
using RoadVision_Backend.Business;
using RoadVision_Backend.Data.DbContextStore;

namespace RoadVision_Backend.Controller
{
    [Route("api/detected-cars")]
    [ApiController]
    public class DetectedCarsController : ControllerBase
    {
        private readonly DetectedCarsBusiness _detectedCarsBusiness;

        public DetectedCarsController(DetectedCarsBusiness detectedCarsBusiness)
        {
            _detectedCarsBusiness = detectedCarsBusiness;
        }

        [HttpPost]
        public async Task<ActionResult<DetectedCar>> Create([FromForm] DetectedCar detectedCar, IFormFile image)
        {
            var result = await _detectedCarsBusiness.AddDetectedCarAsync(
             detectedCar, image);

            return Ok(result);
        }

        [HttpGet]
        public async Task<ActionResult<List<DetectedCar>>> GetAll()
        {
            var cars = await _detectedCarsBusiness.GetAllDetectedCarsAsync();
            return Ok(cars);
        }
    }
}