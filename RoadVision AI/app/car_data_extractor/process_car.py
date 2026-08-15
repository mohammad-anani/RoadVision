from car_data_extractor.plate_number_util.process_plate_number import process_plate_number
from car_data_extractor.car_info_util.classify_car import classify_car


def process_cars(cars):
  """
  Takes the cars images and extracts needed data using AI models
  """

  processed_cars=[]

  for car in cars:
    result = process_car(car)

    if result is not None:
      processed_cars.append(result)
  return processed_cars


def process_car(car):
  car_image=car["best_image"]
 
  plate_result= process_plate_number(car_image)
  car_info_result= classify_car(car_image)

  if plate_result is None and car_info_result is None:
    print("Discarding car #"+str(car["track_id"])+" : Couldn't extract infor or plate number")
    return None

  if plate_result is None:
    print("Car #"+str(car["track_id"])+": Extracted car info only")
    plate_text, plate_text_confidence = None, None
  else:
    plate_text, plate_text_confidence = plate_result

  if car_info_result is None:
    print("Car #"+str(car["track_id"])+": Extracted plate number only")
    car_info, car_info_confidence = None, None
  else:
    car_info, car_info_confidence = car_info_result

  return car,car_info,car_info_confidence,plate_text,plate_text_confidence
