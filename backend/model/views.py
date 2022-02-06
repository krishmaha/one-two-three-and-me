from email.mime import image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import tensorflow as tf
import numpy as np
import json

@csrf_exempt
def predict(request):
  # print(request.body)
  json_body = json.loads(request.body.decode('utf-8'))
  print(json_body['image'])
  new_image = compress(json_body['image']) / 255.0 
  # print(new_image)

  resizedImage = np.reshape(new_image, (1, 28, 28))
  model = tf.keras.models.load_model("/mnt/c/Users/Dhruv/Desktop/ichackproject/backend/model/MNIST_model_trained/")
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
  newimage = np.empty([28, 28])
  image = np.array(image)
  for i in range(0, 559, 20):
    for j in range(0, 559, 20):
      newimage[i // 20][j // 20] = image[i : i + 19][j : j + 19].sum() / 400.
  return newimage