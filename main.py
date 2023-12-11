import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import joblib

st.title('Landmark Recognition')

uploaded_file = st.file_uploader("Choose an image to classify:", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file)
    
    if st.button('Run'):
        
        with st.spinner('AI is running...'):
            cat_clf=joblib.load("model.pkl")

            image = np.asarray(u_img)/255
            my_image= resize(image, (64,64)).reshape((1, 64*64*3)).T
        
            model = load_model('model.pkl')
            
            prediction = model.predict(test_X, verbose=1)
            
            time.sleep(2)
            
            st.success('Done!')

        
    

