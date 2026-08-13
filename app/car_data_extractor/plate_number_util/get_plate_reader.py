from fast_plate_ocr import LicensePlateRecognizer


ocr = LicensePlateRecognizer("cct-xs-v2-global-model")

def get_model():
  """
  Returns the plate reader model
  """
  return ocr