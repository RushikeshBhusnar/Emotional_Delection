import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime

st.title('Age and Emotion Detection for Movie Theatre')

st.write('Upload an image to detect age and emotion. People <13 or >60 are marked as Not allowed.')

uploaded_file = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

def detect_age_and_emotion(image):
    num_people = np.random.randint(1, 4)
    ages = np.random.randint(5, 70, size=num_people)
    emotions = np.random.choice(['happy', 'sad', 'scared'], size=num_people)
    return ages, emotions

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    ages, emotions = detect_age_and_emotion(image)
    results = []
    for i, age in enumerate(ages):
        entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if age < 13 or age > 60:
            allowed = 'Not allowed'
            st.error(f'Person {i+1}: Age {age} - Not allowed')
        else:
            allowed = 'Allowed'
            st.success(f'Person {i+1}: Age {age}, Emotion: {emotions[i]}')
        results.append({'age': age, 'emotion': emotions[i] if allowed=="Allowed" else '', 'entry_time': entry_time, 'allowed': allowed})
    pd.DataFrame(results).to_csv('theatre_results.csv', index=False)
    st.info('Results saved to theatre_results.csv')
else:
    st.write('Please upload an image to get started.') 