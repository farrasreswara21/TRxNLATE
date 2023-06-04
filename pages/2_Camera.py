
import streamlit as st
import numpy as np
import cv2 
from PIL import Image
import requests
import time

st.set_page_config(page_title="Live Camera", page_icon="📷")
st.markdown("# Live Camera 📷")
st.write(
    """
### Put your writing toward the camera, I'll read it for you!"""
)
picture = st.camera_input("Take a picture!")
    
c1, c2= st.columns(2)
if picture is not None:
    img = Image.open(picture)
    img_array = np.array(img)
    cv_image_gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    # prediction on model
    url = 'https://trxnslate-uv7qigoz4a-et.a.run.app/prediction'
    data = cv_image_gray.tolist()
    im = {
        "img_array": data
    }
    
    r = requests.post(url=url, json=im)
    
    c1.header('Predicted Output :')
    c2.header(r.text.split('"')[-2])
    
    time.sleep(1.5)
    st.write("##")
    st.write("##")
    
    rate = st.selectbox('What do you think about the predicted results?',
                    ('','Great!😁', 'Nice try🥲'))
    
    if rate == 'Great!😁':
        st.write('Thankyou!')
    elif rate == 'Nice try🥲': 
        st.write('Sorry...')