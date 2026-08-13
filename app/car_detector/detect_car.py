from car_detector.get_object_detection_model import get_model

def detect_cars(frame):
  """
  Returns the detected objects
  """

  model=get_model()

  results = model.track(
  frame,
  persist=True, # allow tracking to avoid duplicated cars
  tracker="bytetrack.yaml",
  classes=[2, 3, 5, 7],  # car, motorcycle, bus, truck
  conf=0.7, # confidence
  verbose=False # don't log details
  )

  result = results[0]

  return result
