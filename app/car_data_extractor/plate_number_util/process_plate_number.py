from car_data_extractor.plate_number_util.read_plate_number import read_plate_number
from car_data_extractor.plate_number_util.detect_plate_number import detect_plate

def process_plate_number(car_image):
  plate_box=detect_plate(car_image)

  if plate_box is None:
    return None

  plate_image= get_plate_image(car_image,plate_box)

  if plate_image is None:
    return None

  plate_text,prediction_confidence = read_plate_number(plate_image)

  if plate_text is None:
    return None

  return plate_text,prediction_confidence


def get_plate_image(car_image,plate_box):
  x1, y1, x2, y2 = plate_box.xyxy[0].int().tolist()

  plate_image = car_image[y1:y2, x1:x2]

  if plate_image.size == 0:
    return None

  return plate_image
