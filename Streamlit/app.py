import streamlit.components.v1 as components #html extensions
from streamlit_option_menu import option_menu
import streamlit as st
import numpy as np
import base64
from PIL import Image 
from time import sleep
from stqdm import stqdm
from Notebook import teachable_model
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

# def result_output(classes):
#     for classs in classes:
#         if classs[0]==1.0:
#             result=st.subheader("Not a Disease\n Calm your nerves")
#         else:
#             result=st.subheader("High Probability of a Disease\n You should be worried")
#         return result

if page_selection == 'Home Page':
    set_bg_hack('images/giphy2.gif',ext="gif")
    # st.markdown('<style>' + open('icon.css').read() + '</style>', unsafe_allow_html=True)
    original_titl = '<p style="font-family:sans-serif; color:White; font-size: 50px;">Some short intro about the app and what it does would go here</p>'
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
                imagess = Image.open(img_file_buffer,'r')
                st.success("Image uploaded")    
                preview=st.button('Preview')
                if preview:
                    original_title = '<p style="font-family:sans-serif; color:Green; font-size: 50px;">Image Preview</p>'
                    st.markdown(original_title, unsafe_allow_html=True)
                                    
                    st.image(imagess)
                identify = st.button("Identify")
                if identify:
                    result = teachable_model(imagess,"model_weights.h5")
                    with st.sidebar:
                        st.image(imagess)
                        st.subheader(result)

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

