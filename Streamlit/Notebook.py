import tensorflow

import keras
from PIL import Image, ImageOps
import numpy as np
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential, model_from_json
import tensorflow_hub as hub



def teachable_model(img, weight_file):
    #Load Json File, Model Architecture
    json_file = open('mobile_net_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
   
    # Load Model Weights
    loaded_model = model_from_json(loaded_model_json,custom_objects={'KerasLayer':hub.KerasLayer})
    loaded_model.load_weights(weight_file, by_name=True)
    

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(img, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    X =np.expand_dims(image_array,axis=0)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Model target classes in a dictionary
    classes = {0:'Tomatoes Bacterial spot', 1:'Tomatoes Early blight', 2:'Tomatoes Late blight', 
               3:'Tomatoes Leaf Mold', 4:'Tomatoes Septoria leaf spot', 
               5:'Tomatoes Spider mites Two-spotted spider mite', 6:'Tomatoes Target Spot',
               7:'Tomatoes Tomato Yellow Leaf Curl Virus',8:'Tomatoes Tomato mosaic virus',
               9:'Healthy Tomatoe Leaf'}
    
    prediction = loaded_model.predict(X)
    return classes[np.argmax(prediction)] # return position of the highest probability