# Contents of ~/my_app/streamlit_app.py
import streamlit as st
<<<<<<< Updated upstream
=======
import numpy as np
from PIL import Image, ImageOps
import base64
from time import sleep
from stqdm import stqdm


import pickle
from tensorflow import keras
from keras.preprocessing import image as imag


import numpy as np

MODEL = keras.models.load_model("model.h5")

def predictions(input_image):
    #from tensorflow.keras.preprocessing import image as imag
    # img=imag.load_img(input_image , target_size=(224,224))
    size = (224, 224)
    img = ImageOps.fit(input_image, size, Image.ANTIALIAS)

    X = np.asarray(img)
    X =np.expand_dims(X,axis=0)
    
    classes = MODEL.predict(X)
    return classes


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

def result_output(classes):
    for classs in classes:
        if classs[0]==1.0:
            result=st.subheader("Not a Disease\n Calm your nerves")
        else:
            result=st.subheader("High Probability of a Disease\n You should be worried")
        return result

if page_selection == 'Home Page':
    set_bg_hack('images/giphy2.gif',ext="gif")
    # st.markdown('<style>' + open('icon.css').read() + '</style>', unsafe_allow_html=True)
    original_titl = '<p style="font-family:sans-serif; color:White; font-size: 50px;">Leveraging on AI to aid farmers in detecting plant diseases</p>'
    st.markdown(original_titl, unsafe_allow_html=True)


elif page_selection == 'Plant Disease Identifier':
    set_bg_hack('images/bak_img4.jpg',ext="jpg")
    choice =st.selectbox("How would you like to upload your picture",['File Upload', 'Camera'])
    if choice == 'File Upload':

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
                    original_title = '<p style="font-family:sans-serif; color:Green; font-size: 50px;">Image Preview</p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                    st.image(imagess)
                identify = st.button("Identify")
                if identify:
                    classes = predictions(imagess)
                    with st.sidebar:
                        st.image(imagess)
                        result_output(classes)

    if choice == 'Camera':
        
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
   


def sidebar_bg(side_bg):

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
>>>>>>> Stashed changes

#Page Title
st.set_page_config(page_title="AGROSMART AI", page_icon='tomato')

#page background

page_bg_img ="""
<style>
      .stApp {
  background-image: url("https://images.unsplash.com/photo-1612670940073-8aed2145ebc3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OTZ8fHRvbWF0byUyMHdoaXRlJTIwYmFja2dyb3VuZHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=1296&q=60");
  background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def main_page():
    st.title ("Plant Disease Identifier App")
    st.subheader("The app aids in detecting the diseases affecting your plants.")
    #st.markdown("# Main page")
    #st.sidebar.markdown("# Main page")

def page2():
    col1, col2 = st.columns([3,2])
    with col1:
        st.title ("Plant Disease Identifier App")
        image = st.file_uploader("Upload your photo", type=['jpg', 'png'])
        picture = st.camera_input("Take a picture")
        #if picture:
            #st.image(picture)
    with col2:
        st.title ("Results Panel") 
        if image:
            st.success("Image uploaded sucessfully")
            st.image(image) 
        if picture:
            st.success("Image uploaded sucessfully")
            st.image(picture)   
    #st.markdown("# Page 2 ❄️")
    #st.sidebar.markdown("# Page 2")

def page3():
    #st.title ("The Team")
    #st.subheader("The App was created by Explore team 11.")
    st.info("Discover AGROSMART :tomato:")
    #with st.expander(label= f"{tomato}Discover AGROSMART "):
    with st.expander('What we do'):
        st.markdown(
            """
                                    Welcome to AGROSMART! 
            
            We provide AI-driven smart farming and precision agriculture solutions to help farmers save costs and open new business opportunities.
"""
) 
    st.info("Meet The Team!")

    from PIL import Image
    with st.container():
        image = Image.open("/Users/user/Documents/Explore/My practice/Classification app/Team.png")
        st.image(image, use_column_width=True) 
    #st.markdown("# Page 3")
    #st.sidebar.markdown("# Page 3")

page_names_to_funcs = {
    "Main Page": main_page,
    "Plant Disease Identifier": page2,
    "The Team": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()