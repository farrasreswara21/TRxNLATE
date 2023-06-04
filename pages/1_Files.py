
import streamlit as st
import numpy as np
import cv2 
from PIL import Image
import requests
import time

st.set_page_config(page_title="Upload Files", page_icon="📂")

st.markdown("# Upload Files 📂")
st.write(
    """### Upload your files and we will read it for you!"""
)
upload= st.file_uploader('Insert image to read (png or jpg)', type=['png','jpg'])

c1, c2= st.columns(2)
if upload is not None:
    im1= Image.open(upload).convert('RGB')
    cv_image = np.array(im1)
    cv_image_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    c1.header('Input Image')
    c1.image(cv_image_gray)
    
    # # prediction on model
    url = 'https://trxnslate-uv7qigoz4a-et.a.run.app/prediction'
    data = cv_image_gray.tolist()
    im = {
        "img_array": data
    }
    r = requests.post(url=url, json=im)
    
    c2.header('Predicted Output')
    c2.header(r.text.split('"')[-2])
    time.sleep(1.5)
    st.write("##")
    st.divider()
    
    rate = st.selectbox('What do you think about the predicted results?',
                    ('','Great!😁', 'Nice try🥲'))
    
    if rate == 'Great!😁':
        st.write('Thankyou!')
    elif rate == 'Nice try🥲': 
        st.write('Sorry...')
    


