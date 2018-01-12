import numpy as np
#import Image
#from PIL import Image
from PIL import Image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.applications import imagenet_utils
model = VGG16(weights='imagenet', include_top=True)
layers = dict([(layer.name, layer.output) for layer in model.layers])
#print(layers) 
image_path = 'images/duck.jpg'
image = Image.open(image_path)
image = image.resize((224, 224))
# Convert it into an array
x = np.asarray(image, dtype='float32')
# Convert it into a list of arrays
x = np.expand_dims(x, axis=0)
# Pre-process the input to match the training data
x = preprocess_input(x)

preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
