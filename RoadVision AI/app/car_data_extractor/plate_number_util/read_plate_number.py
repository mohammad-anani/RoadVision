# from get_plate_reader import get_model
from car_data_extractor.plate_number_util.get_plate_reader import get_model

MIN_CONFIDENCE = 0.5

def read_plate_number(plate_image):
  """
  Returns:
    str: detected plate number if confidence >= 0.5
    None: if no text is detected or confidence is too low
  """

  model = get_model()

  result = model.run(
    plate_image,
    return_confidence=True
  )

  if not result:
    return None

  prediction = result[0]

  if not prediction.has_confidence or len(prediction.char_probs)==0:
    return None

  confidence = get_avg_confidence(prediction)

  if confidence < MIN_CONFIDENCE:
    return None

  return (prediction.plate, confidence)


def get_avg_confidence(prediction):
  return sum(prediction.char_probs) / len(prediction.char_probs)


## Testing
# import numpy as np
# from PIL import Image

# image = Image.open("input/plate_image_test.png").convert("RGB")
# img_array = np.array(image)

# text, conf = read_plate_number(img_array)

# print(text, conf)