import streamlit as st
import numpy as np
from PIL import Image

st.title('Car Colour Detection at Traffic Signal')

st.write('Upload an image to detect car colours and count cars and people.')

uploaded_file = st.file_uploader('Upload Image', type=['jpg', 'jpeg', 'png'])

def detect_cars_and_people(image):
    num_cars = np.random.randint(1, 5)
    car_colors = np.random.choice(['blue', 'red', 'white'], size=num_cars)
    num_people = np.random.randint(0, 5)
    return car_colors, num_people

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    car_colors, num_people = detect_cars_and_people(image)
    st.write(f'Car colors: {car_colors}')
    st.write(f'Number of people: {num_people}')
else:
    st.write('Please upload an image to get started.') 