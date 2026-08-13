from car_data_extractor.plate_number_util.get_plate_detection_model import get_model

plate_detector = get_model()

MIN_CONFIDENCE=0.5

def detect_plate(car_image):
  """
  Returns the box of the first detected plate
  """

  results = plate_detector(car_image, conf=MIN_CONFIDENCE, verbose=False)

  for result in results:
    if result.boxes is None or len(result.boxes) == 0:
      return None

    box = result.boxes[0]
    return box