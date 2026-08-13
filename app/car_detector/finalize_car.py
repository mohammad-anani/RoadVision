import time
import cv2

MISSING_TIMEOUT = 10  # seconds

def remove_and_get_finalized_tracked_cars(tracked_cars):
  """
  Considers a car image ready to process after its last seen image hits a certain timeout value 
  """

  current_time = time.monotonic()
  cars_crossing_timeout = []

  # Prepare cars that have crossed the missing timeout value
  for track_id, car in tracked_cars.items():
    time_missing = current_time - car["last_seen"]
    if time_missing >= MISSING_TIMEOUT:
      cars_crossing_timeout.append(car)

  # Pop the car from tracking, after getting finalized
  for car in cars_crossing_timeout:
    car = tracked_cars.pop(car["track_id"])

  return cars_crossing_timeout