import cv2


def prepare_request(processed_car):
  car, car_info, car_info_confidence, plate_text, plate_text_confidence = processed_car

  success, encoded_image = cv2.imencode(".jpg", car["best_image"])

  if not success:
    raise ValueError("Failed to encode car image")

  image_bytes = encoded_image.tobytes()

  form_data = {
    "carInfo": car_info["class_name"] if car_info is not None else "",
    "carInfoConfidence": str(car_info_confidence) if car_info_confidence is not None else None ,
    "plateNumber": plate_text,
    "plateNumberConfidence": str(plate_text_confidence) if plate_text_confidence is not None else None,
    "detectedAt": str(car["best_time"]),
    "imagePath":None
  }

  files = {
    "image": ("car.jpg", image_bytes, "image/jpeg")
  }

  return form_data, files