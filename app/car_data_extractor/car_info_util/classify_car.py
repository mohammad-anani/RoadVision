import numpy as np
from PIL import Image
from car_data_extractor.car_info_util.get_car_classification_model import get_model
import csv


car_classifier = get_model()


# This process is based on the model worflow documented by its author
def classify_car(car_image):
  """
  Returns predicted info about the car(model, make, year) 
  """

  image = Image.fromarray(car_image).convert("RGB")

  image = image.resize((380, 380))

  image = np.array(image).astype(np.float32) / 255.0

  image = (
    image - np.array([0.485, 0.456, 0.406])
  ) / np.array([0.229, 0.224, 0.225])

  image = image.transpose(2, 0, 1)

  image = np.expand_dims(image, axis=0)

  outputs = car_classifier.run(
    None,
    {
      "input": image
    }
  )

  logits = outputs[0]

  probabilities = np.exp(logits) / np.sum(
    np.exp(logits),
    axis=1,
    keepdims=True
  )

  best_index = np.argmax(probabilities[0])

  confidence = float(probabilities[0][best_index])

  return get_index_info(index), confidence


def get_index_info(index):

  if index is None:
    return None

  with open("models/class_mapping.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
      if int(row["index"]) == index:
        return row

  return None