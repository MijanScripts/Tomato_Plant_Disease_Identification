from turtle import width
import streamlit.components.v1 as components #html extensions
from streamlit_option_menu import option_menu
import streamlit as st
import numpy as np
import base64
import io
from PIL import Image 
from time import sleep
from stqdm import stqdm
from Notebook import teachable_model
import webbrowser


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
    # INTRO ON HOMEPAGE
    original_titl = '<p style="font-family:sans-serif; color:White; font-size: 60px;">Welcome to Tomato Plant Disease Identifier AI...</p>'
    st.markdown(original_titl, unsafe_allow_html=True)
    original_titl1 = '<p style="font-family:sans-serif; color:White; font-size: 30px;">Discover Machine Learning technology that aids you in detecting tomato plant diseases.</p>'
    st.markdown(original_titl1, unsafe_allow_html=True)


                    
elif page_selection == 'Plant Disease Identifier':
    set_bg_hack('images/bak_img4.jpg',ext="jpg")
    choice =st.selectbox("How would you like to upload your picture",['File Upload', 'Camera'])
    if choice == 'File Upload':
        
        # img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
        uploaded_files = st.file_uploader("Upload an Image",type=['jpg','jpeg','png'],help="You can only upload images in the format .jpg, .jpeg, .png", accept_multiple_files=True,)
        with st.expander("Preview Images"):
            jpegs =[]
            for i in uploaded_files:
                jpegs.append(i)
            st.image(jpegs,width=100)        # preview = st.button("Preview")
 
        if st.button("Click Here To Classify"):
            if uploaded_files is not None:
                l=[]
                n=[]
                for uploaded_file in uploaded_files:
                    bytes_datas = uploaded_file.read()
                    images = Image.open(io.BytesIO(bytes_datas))
                    with st.spinner("Classifying...."):
                        result = teachable_model(images,"model_weights.h5")
                        l.append(result)
                        n.append(images)
                st.success("Done")
                for i in range(len(l)):
                    with st.sidebar:
                        st.image(n[i])
                        st.subheader(l[i])
                            
            elif uploaded_files[0] is None:
                st.subheader("Please Upload an Image to Classify")
    

    if choice == 'Camera':
        
        img_camera_buffer = st.camera_input("Take a Picture")
        if st.button("Click Here To Classify"):

            if img_camera_buffer is not None:
                l=[]
                n=[]
                images = Image.open(img_camera_buffer)
                with st.spinner("Classifying...."):
                    result = teachable_model(images,"model_weights.h5")
                    l.append(result)
                    n.append(images)
                    st.success("Done")
                    for i in range(len(l)):
                        with st.sidebar:
                            st.image(n[i])
                            st.subheader(l[i])
                
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

# THE ABOUT PAGE
elif page_selection == 'About':
    set_bg_hack('images/bak_img4.jpg',ext="jpg")
    def header(url):
        option = st.markdown(f'<p style="color:white;font-size:15px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        return option
    header('Discover AGROSMART ')


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
        image = Image.open("Team.png")
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

