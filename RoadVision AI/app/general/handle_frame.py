from car_detector.detect_car import detect_cars
from car_detector.track_car import update_tracked_cars
from car_detector.finalize_car import remove_and_get_finalized_tracked_cars
from car_data_extractor.process_car import process_cars
from car_inserter.insert_car import insert_cars

tracked_cars={}

def handle_frame(frame):
  """
  Process the frame as needed. Returns handled frame 
  """

  result= detect_cars(frame)

  update_tracked_cars(result,tracked_cars, frame)

  cars_to_process= remove_and_get_finalized_tracked_cars(tracked_cars)

  cars_to_insert= process_cars(cars_to_process)

  insert_cars(cars_to_insert)

  frame_with_outlined_objects= result.plot()

  return frame_with_outlined_objects