import onnxruntime as ort

model=ort.InferenceSession(
    "models/vehicle_classifier.onnx")
    
def get_model():
  return model