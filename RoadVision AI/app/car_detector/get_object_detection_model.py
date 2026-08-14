from ultralytics import YOLO

model = YOLO("models/yolo11n.pt")

def get_model():
  """
  Returns the object detection model
  """
  return model