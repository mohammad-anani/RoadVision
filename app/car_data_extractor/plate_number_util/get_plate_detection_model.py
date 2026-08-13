from ultralytics import YOLO

model = YOLO("models/license_plate_detector.pt")

def get_model():
  """
  Returns the plate detection model
  """
  return model