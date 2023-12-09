import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title('Landmark Recognition')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.image(uploaded_file)
    
    if st.button('Run'):
        st.write('AI is running...')
