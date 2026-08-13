from car_data_extractor.plate_number_util.process_plate_number import process_plate_number
from car_data_extractor.car_info_util.classify_car import classify_car

def process_cars(cars,frame):
  """
  Takes the cars images and extracts needed data using AI models
  """

  for car in cars:
    process_car(car,frame)


def process_car(car,frame):
  car_image=get_car_image(car,frame)
 
  plate_text, plate_prediction_confidence= process_plate_number(car_image)

  car_info, car_info_confidence= classify_car(car_image)

  pritn(car_info, plate_text)
  



def get_car_image(car,frame):
  x1,y1,x2,y2=car["best_box"]

  car_image= frame[y1:y2,x1:x2]

  return car_image

