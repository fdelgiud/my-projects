import streamlit as st
import librosa
import librosa.display
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from streamlit_mic_recorder import mic_recorder

# Streamlit Page Configuration
st.set_page_config(page_title="Real-Time Speech Recognition", layout="centered")

# Load the trained model
model_mfcc = tf.keras.models.load_model("speech_recognition_model_mfcc_1.h5")

# Define class labels (Modify according to your dataset)
class_labels = [
    'bed', 'bird', 'cat', 'dog', 'down', 'eight', 'five', 'four', 'go', 'happy', 'house',
    'left', 'marvel', 'nine', 'no', 'off', 'on', 'one', 'right', 'seven', 'sheila', 'six',
    'stop', 'three', 'tree', 'two', 'up', 'wow', 'yes', 'zero']

# Function to extract MFCC features
def extract_mfcc(audio_data, sr=16000, max_pad=40):
    try:
        # MFCC extraction
        mfcc = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)

        # Padding or truncating MFCCs
        if mfcc.shape[1] < max_pad:
            pad_width = max_pad - mfcc.shape[1]
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
        else:
            mfcc = mfcc[:, :max_pad]

        return mfcc  # Return MFCC
    except Exception as e:
        print(f"Error processing audio: {e}")
        return None

# Streamlit app UI
st.title("🎙️ Real-Time Speech Recognition")

# Option to upload an audio file
audio_file = st.file_uploader("Upload an audio file (WAV format)", type=["wav"])

# Option to record audio from microphone
recorded_audio = mic_recorder(start_prompt="🎤 Start Recording", stop_prompt="⏹️ Stop Recording", key="recorder")

# Initialize MFCC variable
mfcc = None
y = None  # to store audio data for plotting

# Check if audio is uploaded or recorded
if audio_file is not None:
    st.audio(audio_file, format="audio/wav")
    # Read audio from file
    y, sr = librosa.load(audio_file, sr=16000)
    mfcc = extract_mfcc(y, sr)

elif recorded_audio is not None:
    st.audio(recorded_audio, format="audio/wav")
    
    # Convert recorded audio (which may be in a different format) to numpy array
    audio_data, sr = librosa.load(recorded_audio, sr=16000)
    mfcc = extract_mfcc(audio_data, sr)
    y = audio_data  # Use the recorded audio data for plotting

else:
    st.warning("Please upload or record an audio file to proceed.")

# If MFCC is successfully extracted, proceed with model prediction
if mfcc is not None and y is not None:
    # Display the waveform and MFCC
    fig, ax = plt.subplots(2, 1, figsize=(10, 6))

    # Plot the waveform
    ax[0].set_title("Waveform")
    librosa.display.waveshow(y, sr=sr, ax=ax[0])

    # Plot the MFCC
    ax[1].set_title("MFCC")
    img = librosa.display.specshow(mfcc, x_axis='time', sr=sr, ax=ax[1])

    # Add colorbar to the MFCC plot
    fig.colorbar(img, ax=ax[1])

    # Show the plots
    st.pyplot(fig)

    # Prepare MFCC for prediction
    mfcc = np.expand_dims(mfcc, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model_mfcc.predict(mfcc)
    predicted_class = np.argmax(prediction)  # Get the class index
    confidence = np.max(prediction)  # Get confidence score

    # Get the predicted label
    predicted_label = class_labels[predicted_class]

    # Display the classification result
    st.subheader("📝 Speech Recognition Result:")
    st.write(f"**Predicted Class:** {predicted_label}")
    st.write(f"**Confidence Score:** {confidence:.2f}")



