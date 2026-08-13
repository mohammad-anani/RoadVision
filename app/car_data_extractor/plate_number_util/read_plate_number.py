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

  if prediction.confidence < MIN_CONFIDENCE:
    return None

  return (prediction.text,prediction.confidence)