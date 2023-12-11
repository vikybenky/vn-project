import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import cv2


st.title('Landmark Recognition')

uploaded_file = st.file_uploader("Choose an image to be uploaded:", type="jpg")

IMG_SIZE = 64 

def img_load(img): 
    img = img/255.
    img_redim = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
    return img_redim
    
if uploaded_file is not None:
    st.image(uploaded_file)
    
    if st.button('Run'):
        st.write('AI is running...')

        model = load_model('my_model.h5')
        X_prepared = []
        X_prepared.append(img_load(uploaded_file))
        X_prepared = np.array(X_prepared)
        prediction = model.predict(test_X, verbose=1) 
