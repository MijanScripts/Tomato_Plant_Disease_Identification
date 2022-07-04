# Contents of ~/my_app/streamlit_app.py
import streamlit as st

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