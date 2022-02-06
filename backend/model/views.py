from email.mime import image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import tensorflow as tf
import numpy as np
import json

@csrf_exempt
def predict(request):
  json_body = json.loads(request.body.decode('utf-8'))
  new_image = compress(json_body['image'])

  resizedImage = np.reshape(new_image, (1, 28, 28))

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
