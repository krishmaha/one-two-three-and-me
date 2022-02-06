from email.mime import image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import tensorflow as tf
import numpy as np
import json
from matplotlib import pyplot as plt

@csrf_exempt
def predict(request):
  json_body = json.loads(request.body.decode('utf-8'))
  print(json_body['image'])
  new_image = compress(json_body['image'])

  resizedImage = np.reshape(new_image, (1, 28, 28))
  # print(np.reshape(resizedImage, (28, 28)).tolist())

  model = tf.keras.models.load_model("model/MNIST_model_trained/")
  prediction = model.predict(resizedImage)
  predicted_number = prediction.argmax()
  score = prediction[0][predicted_number] / prediction.sum()

  response = JsonResponse({
    "predicted": int(predicted_number),
    "score": float(score)
  })

  response['Access-Control-Allow-Origin'] = '*'

  return response;

# def compress(image):
#   new_image = np.empty([28, 28])
#   for i in range(0, len(image) - 1, 20):
#     for j in range(0, len(image) - 1, 20):
#       sumvalue = 0
#       for r in range(0, 19):
#         for k in range(0, 19):
#           sumvalue += image[i + r][j + k]
#       avgvalue = (sumvalue / 400.) ** 2
#       new_image[(i + 1) // 20][(j + 1) // 20] = avgvalue 
#   return new_image

# def compress(image):
#   new_image = np.empty([28, 28])
#   for i in range(0, len(image) - 1, 20):
#     for j in range(0, len(image) - 1, 20):
#       newvalue = 0
#       for r in range(0, 19):
#         for k in range(0, 19):
#           if (image[i + r][j + k] > 0): newvalue = 255
#       new_image[(i + 1) // 20][(j + 1) // 20] = newvalue
#   return new_image

def compress(image):
  new_image = np.empty([28, 28])
  for i in range(0, len(image) - 1, 20):
    for j in range(0, len(image) - 1, 20):
      sumvalue = 0
      for r in range(0, 19, 4):
        for k in range(0, 19, 4):
          sumvaluesmall = 0
          for v in range(0, 4):
            for w in range(0, 4):
              sumvaluesmall += image[i + r + v][j + k + w]
          avgvaluesmall = sumvaluesmall / 16.
          sumvalue += avgvaluesmall
      avgvalue = (sumvalue / 25) ** 2
      new_image[(i + 1) // 20][(j + 1) // 20] = avgvalue 
  return new_image
