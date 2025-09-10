import streamlit as st
import numpy as np
import librosa

st.title('Voice Emotion Detection (Female Only)')

st.write('Upload or record a voice note to detect emotion. Only female voices are accepted.')

uploaded_file = st.file_uploader('Upload Audio', type=['wav', 'mp3'])

def extract_features(audio_bytes):
    # Dummy: return random features
    return np.random.rand(40)
def predict_emotion(features):
    return np.random.choice(['happy', 'sad', 'angry'])
def is_female_voice(features):
    return np.random.choice([True, False])

if uploaded_file is not None:
    audio_bytes = uploaded_file.read()
    st.audio(audio_bytes, format='audio/wav')
    features = extract_features(audio_bytes)
    if is_female_voice(features):
        emotion = predict_emotion(features)
        st.success(f'Emotion: {emotion}')
    else:
        st.error('Please upload a female voice.')
else:
    st.write('Please upload an audio file to get started.') 