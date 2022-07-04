#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pickle
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


pickled_model = pickle.load(open('model.pkl', 'rb'))


# In[10]:


MODEL = keras.models.load_model("model.h5")


# In[7]:


img = image.load_img("images/bak_img5.jpg")


# In[56]:


dir_path = "images/healthy_img.jpg"


img=image.load_img(dir_path , target_size=(224,224))

    
X = image.img_to_array(img)
X =np.expand_dims(X,axis=0)

    
classes = model.predict(X)
# if classes == 0:
#     print("You look Happy \n You must be having a Good day!")
# else:
#     print('You Do not Look Happy \n Is Everything Okay?')
    


# In[57]:


out = classes.tolist()


# In[58]:


for i in classes:
    print(i)
    for n in i:
        print(n)
    


# In[55]:


img


# In[ ]:

def predictions(input_image):

    img=image.load_img(input_image , target_size=(224,224))

    X = image.img_to_array(img)
    X =np.expand_dims(X,axis=0)
    
    classes = MODEL.predict(X)
    return classes


