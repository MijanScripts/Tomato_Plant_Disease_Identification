from sqlalchemy import null
import streamlit.components.v1 as components #html extensions
from streamlit_option_menu import option_menu
import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import base64
from time import sleep
from stqdm import stqdm


import pickle
from tensorflow import keras
import tensorflow_hub as hub
from keras.models import model_from_json
from keras.preprocessing import image as imag
import numpy as np

# load json and create model
def teachable_model(img, weight_file):
    json_file = open('mobile_net_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json,custom_objects={'KerasLayer': hub.KerasLayer})
    # Creating a model using json 
    loaded_model.load_weights(weight_file)
    
  # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(null, 224, 224, 3), dtype=np.float32)
    image = img

    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    X =np.expand_dims(image_array,axis=0)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # predicting using the processed image data in the form of an array
    prediction = loaded_model.predict(X)
    return prediction # return position of the highest probability

# URL for Mobilenet model
URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/2"
#MODEL = keras.models.load_model("mobile_net_model.h5", custom_objects={'KerasLayer': hub.KerasLayer(URL, input_shape = (224, 224, 3))})

#def predictions(input_image):
    #from tensorflow.keras.preprocessing import image as imag
    # img=imag.load_img(input_image , target_size=(224,224))
    #size = (224, 224)
    #img = ImageOps.fit(input_image, size, Image.ANTIALIAS)

    #X = np.asarray(img)
    #X =np.expand_dims(X,axis=0)
    
    #classes = MODEL.predict(X)
    #return classes

# Setting up the background on Streamlit app
st.set_page_config(page_title="PlantAI", page_icon='tree-fill')

def set_bg_hack(main_bg, ext):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = ext
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Setting up the options menu
page_selection = option_menu(
        menu_title = "TOMATO PLANT DISEASE IDENTIFIER APP", 
        options = ["Home Page","Plant Disease Identifier","About"],
        icons = ['house', 'tree-fill','envelope'],
        menu_icon='tomato',
        default_index= 0,
        orientation='horizontal',
        styles={"container":{'padding':'0!important', 'background_color': '#011103'},
            'icon': {'color': 'green', 'font-size': '20px'},
            'nav-link': {
                'font-size':'15px',
                'text-align': 'center',
                'margin': '2px',
                '--hover-color': '#9DE3A9',
            },
            'nav-link-selected': {'background-color': '#04AD21'},
        }
    )
# predicting whether leaf is healthy or not after uploading an image
def result_output(prediction):
    for predict in prediction:
        if predict[0]==1.0:
            result=st.subheader("Not a Disease\n Calm your nerves")
        else:
            result=st.subheader("High Probability of a Disease\n You should be worried")
        return result
        
'''The code below sets up the Home page, Plant Identier page and About page. 
    Creates a provison for either taking a photo of the leaf or uploading a 
    photo from saved files on the identifier page. '''

if page_selection == 'Home Page':
    set_bg_hack('images/giphy2.gif',ext="gif")
    # st.markdown('<style>' + open('icon.css').read() + '</style>', unsafe_allow_html=True)
    original_titl = '<p style="font-family:sans-serif; color:White; font-size: 50px;">Leveraging on AI to aid farmers in detecting plant diseases</p>'
    st.markdown(original_titl, unsafe_allow_html=True)

elif page_selection == 'Plant Disease Identifier':
    set_bg_hack('images/bak_img4.jpg',ext="jpg")
    choice =st.selectbox("How would you like to upload your picture",['File Upload', 'Camera'])
    if choice == 'File Upload': # Uploading from saved files

        img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        
        if img_file_buffer is not None:
            c1,c2 = st.columns([2,1])
            with c1:
                
                image_data = img_file_buffer.read()
                # img = imag.load_img(image_data)
                imagess = Image.open(img_file_buffer)
                st.success("Image uploaded")    
                preview=st.button('Preview')
                if preview:
                    original_title = '<p style="font-family:sans-serif; color:white; font-size: 15px;">Image Preview</p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                    st.image(imagess)
                identify = st.button("Identify")
                if identify:
                    classes = teachable_model(imagess, weight_file=keras.models.load_model("mobile_net_model.h5", custom_objects={'KerasLayer': hub.KerasLayer(URL, input_shape = (224, 224, 3))}))
                    with st.sidebar:
                        st.image(imagess)
                        result_output(classes)

    if choice == 'Camera': # Capturing a photo
        
        img_camera_buffer = st.camera_input("Take a Picture")
        if img_camera_buffer is not None:
            image = np.array(Image.open(img_camera_buffer))
            c1,c2 = st.columns([2,1])
            with c1:
                image = np.array(Image.open(img_camera_buffer))    
                
                st.success("Image uploaded")
                preview=st.button('Preview')
                if preview:
                    st.title("Image Preview")
                    st.image(image)
                identify = st.button("Identify")
                if identify:
                    with st.sidebar:
                        st.image(image)
                        result_output()
                
    # with open("pil.html",'r') as f:
    #     pil_string = f.read()
    pil_string = """<html>
                    <head>
                        <meta charset="utf-8">
                        <title>Content Boxes In HTML</title>
                        <link rel="stylesheet" type='text/css' href="style.css">
                    </head>
                    <body>
                        <div class="container">
                            <div class="box"></div>
                            <div class="box"></div>
                            <div class="box"></div>
                        </div>
                    </body>
                    </html>"""
    components.html(pil_string)
    # st.markdown(html_string,unsafe_allow_html=True)

elif page_selection == 'About':
    set_bg_hack('images/giphy2.gif',ext="gif")
    st.info("Discover AGROSMART :tomato:")
        #st.markdown(f'<p style="font-family:sans-serif; color:White; font-size: 50px;">Discover AGROSMART :tomato:</p>', unsafe_allow_html=True)
    #with st.expander(label= f"{tomato}Discover AGROSMART "):
    with st.expander('What we do'):
        st.markdown(f'<p style="font-family:sans-serif; color:White; font-size: 12px;">Welcome to AGROSMART! </p>', unsafe_allow_html=True) 
        st.markdown(f'<p style="font-family:sans-serif; color:White; font-size: 12px;">We provide AI-driven smart farming and precision agriculture solutions to help farmers save costs and open new business opportunities.</p>', unsafe_allow_html=True)
    st.info("Meet The Team!")

    from PIL import Image
    with st.container():
        image = Image.open("/Users/user/Documents/GitHub/Tomato_Plant_Disease_Identification/Streamlit/Team1.png")
        st.image(image, use_column_width=True) 
   


def sidebar_bg(side_bg): # a sidebar that shows predicted results

   side_bg_ext = 'jpg'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )

