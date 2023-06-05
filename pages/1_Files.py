
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
    
    output = r.text.split('"')[-2]
    c2.header('Predicted Output')
    c2.header(output)
    
    # Upload image
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'doctorrx-387716-cdaefd627b4a.json'

    client = storage.Client()

    bucket = client.get_bucket('doctorrx_pipeline_bucket')
    image = cv_image
    with TemporaryFile() as gcs_image:
        image.tofile(gcs_image)
        gcs_image.seek(0)
        blob = bucket.blob(f'data_unlabelled/YES/{output}/{random.randrange(000000, 999999)}.png')
        blob.upload_from_file(gcs_image)
    
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
    


