import keras
from keras.models import load_model
from PIL import Image
import numpy as np

model1 = load_model('MNIST_keras_CNN.h5')

image = Image.open('stuid2.jpg').convert('L')
image = image.resize((28, 28))
image = np.array(image)
image = image.reshape(1, 28, 28, 1)
image = image.astype('float32')
image /= 255

# Use the model to make a prediction
prediction = model1.predict(image)

# Print the predicted label
predicted_label = np.argmax(prediction)
print('Predicted label:', predicted_label)
