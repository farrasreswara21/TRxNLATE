
import streamlit as st
import numpy as np
import cv2 
from PIL import Image

import random
import requests
import time
import os

from google.cloud import storage
from tempfile import TemporaryFile

st.set_page_config(page_title="Live Camera 📸", page_icon="📷")
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
    
    output = r.text.split('"')[-2]
    c1.header('Predicted Output :')
    c2.header(output)
    
    # Upload image
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'doctorrx-387716-cdaefd627b4a.json'

    client = storage.Client()

    bucket = client.get_bucket('doctorrx_pipeline_bucket')
    image = img_array
    success, encoded_image = cv2.imencode('.png', image)
    content2 = encoded_image.tobytes()

    # di save
    blob = bucket.blob(f'data_unlabelled/YES/{output}/{random.randrange(000000, 999999)}.png')
    blob.upload_from_string(content2)

    
    #Feedback
    time.sleep(1.5)
    st.write("##")
    st.divider()
    
    rate = st.selectbox('What do you think about the predicted results?',
                    ('','Great!😁', 'Nice try🥲'))
    
    if rate == 'Great!😁':
        st.write('Thankyou!')
    elif rate == 'Nice try🥲': 
        st.write('Sorry...')