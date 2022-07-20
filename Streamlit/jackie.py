import streamlit.components.v1 as components #html extensions
from streamlit_option_menu import option_menu
import streamlit as st
import io
import numpy as np
from PIL import Image, ImageOps
import base64
from time import sleep
from stqdm import stqdm

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
        })

if page_selection == 'Home Page':
    set_bg_hack('images/giphy2.gif',ext="gif")
    # st.markdown('<style>' + open('icon.css').read() + '</style>', unsafe_allow_html=True)
    original_titl = '<p style="font-family:sans-serif; color:White; font-size: 50px;">Some short intro about the app and what it does would go here</p>'
    st.markdown(original_titl, unsafe_allow_html=True)

elif page_selection == 'Plant Disease Identifier':
    set_bg_hack('images/bak_img4.jpg',ext="jpg")
    add_image = st.radio('Add Image', ('File Upload', 'Camera'))
    if add_image == 'File Upload':
        img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
        if img_file_buffer is not None:
            for img in img_file_buffer:
                image = np.array(Image.open(img))
                c1,c2 = st.columns([2,1])
                with c1:
                    image = np.array(Image.open(img))    
                
                    st.success("Image uploaded")
                    preview=st.button('Preview')
                    if preview:
                        st.title("Image Preview")
                        st.image(image)
                    identify = st.button("Identify")
                    if identify:
                        with st.sidebar:
                            st.image(image)
                            st.write('leaves')
        
    if add_image == 'Camera':
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
                        st.write('leaves')
    #with st.sidebar:
        #if image:
            #st.success("Image uploaded sucessfully")
            #st.image(image) 
        #if picture:
            #st.success("Image uploaded sucessfully")
            #st.image(picture)'''   
   
                
