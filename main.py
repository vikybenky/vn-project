import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title('Landmark Recognition')

uploaded_file = st.file_uploader("Choose an image to be uploaded:", type="jpg")

if uploaded_file is not None:
    st.image(uploaded_file)
    
    if st.button('Run'):
        st.write('AI is running...')

        model = load_model('my_model.h5')
        prediction = model.predict(test_X, verbose=1) 
