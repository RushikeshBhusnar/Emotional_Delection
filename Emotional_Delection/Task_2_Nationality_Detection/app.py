import streamlit as st
from PIL import Image
import numpy as np
import cv2
from keras.models import model_from_json
import os

st.title('Nationality, Emotion, Age, and Dress Color Detection')

# Load emotion model (load once)
@st.cache_resource
def load_emotion_model():
    with open(os.path.join('..', 'model_a1.json'), 'r') as json_file:
        loaded_model_json = json_file.read()
    model = model_from_json(loaded_model_json)
    model.load_weights(os.path.join('..', 'model_weights1.h5'))
    return model

emotion_model = load_emotion_model()
emotion_classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def predict_nationality(image):
    # Dummy logic: always returns 'Indian'
    return 'Indian'
def predict_age(image):
    # Dummy logic: random age
    return np.random.randint(18, 40)
def predict_dress_color(image):
    # Dummy logic: always returns 'Red'
    return 'Red'

def preprocess_image(image):
    img = np.array(image.convert('L'))  # Convert to grayscale
    img = cv2.resize(img, (48, 48))
    img = img / 255.0
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    return img

uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write('Processing...')
    img = preprocess_image(image)
    # Emotion prediction
    emotion_pred = emotion_model.predict(img)
    emotion_label = emotion_classes[np.argmax(emotion_pred)]
    # Nationality, age, dress color
    nationality = predict_nationality(img)
    age = predict_age(img)
    dress_color = predict_dress_color(img)
    st.write(f'**Nationality:** {nationality}')
    st.write(f'**Emotion:** {emotion_label}')
    if nationality == 'Indian':
        st.write(f'**Age:** {age}')
        st.write(f'**Dress Color:** {dress_color}')
    elif nationality == 'United States':
        st.write(f'**Age:** {age}')
    elif nationality == 'African':
        st.write(f'**Dress Color:** {dress_color}')
else:
    st.write('Please upload an image to get started.') 