import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.title('Drowsiness Detection in Vehicle')

st.write('Upload an image or video to detect sleeping people and their ages.')

uploaded_file = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

# Dummy detection logic
def detect_people_and_drowsiness(image):
    num_people = np.random.randint(1, 4)
    boxes = [np.random.randint(0, min(image.size), size=4) for _ in range(num_people)]
    drowsy = np.random.choice([True, False], size=num_people)
    ages = np.random.randint(18, 50, size=num_people)
    return boxes, drowsy, ages

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    img = np.array(image)
    boxes, drowsy, ages = detect_people_and_drowsiness(image)
    sleeping_count = sum(drowsy)
    sleeping_ages = [ages[i] for i in range(len(ages)) if drowsy[i]]
    st.success(f'Sleeping people: {sleeping_count}, Ages: {sleeping_ages}')
else:
    st.write('Please upload an image to get started.') 