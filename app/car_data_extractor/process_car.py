from car_data_extractor.plate_number_util.process_plate_number import process_plate_number
from car_data_extractor.car_info_util.classify_car import classify_car

def process_cars(cars):
  """
  Takes the cars images and extracts needed data using AI models
  """

  for car in cars:
    process_car(car)


def process_car(car):
  car_image=car["best_image"]
 
  plate_result= process_plate_number(car_image)

  if plate_result is None:
    return

  plate_text, plate_prediction_confidence=plate_result
  
  car_info, car_info_confidence= classify_car(car_image)

  print(car['track_id'],plate_text,plate_prediction_confidence)