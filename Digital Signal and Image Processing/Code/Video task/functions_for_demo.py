# Import necessary libraries
import cv2
import numpy as np
import time
import tkinter as tk
from tkinter import filedialog
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import imageio
from IPython.display import Image, display
import os 

#------------
def load_frames_from_folder(folder_path):
    """
    Loads frames from a folder and returns them as a list of numpy arrays.

    Parameters:
        folder_path (str): The path to the folder containing the frames.

    Returns:
        list: A list of frames loaded as numpy arrays.
    """
    frames = []
    for frame_file in sorted(os.listdir(folder_path)):  
        frame_path = os.path.join(folder_path, frame_file)
        if frame_file.endswith(('.jpg', '.png', '.jpeg')):  
            frame = cv2.imread(frame_path)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converti in RGB
            frames.append(frame)
    return frames

def create_gif_from_frames(frames, gif_path, duration=0.1):
    """
    Creates a GIF from a sequence of frames and saves it to the specified path.

    Parameters:
        frames (list): A list of frames (numpy arrays) to include in the GIF.
        gif_path (str): The path where the GIF will be saved.
        duration (float): Duration of each frame in the GIF, in seconds.
    """
    # Create and save GIF
    with imageio.get_writer(gif_path, mode="I", duration=duration) as writer:
        for frame in frames:
            writer.append_data((frame).astype(np.uint8))  # Scala da [0, 1] a [0, 255]

def generate_and_save_gifs(videos, output_folder, duration=0.2):
    """
    Generates GIFs for videos and saves them to a specified folder.

    Parameters:
        videos (dict): A dictionary where the keys are video class names and the values are file paths to the videos.
        output_folder (str): Path to the folder where the GIFs will be saved.
        duration (float): Duration of each frame in the GIF, in seconds.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for class_name, video_path in videos.items():
        frames = load_frames_from_folder(video_path)
        gif_path = os.path.join(output_folder, f"{class_name.replace(' ', '_')}_animation.gif")
        
        # Create and save GIF
        create_gif_from_frames(frames, gif_path, duration)
        print(f"GIF saved for '{class_name}' in: {gif_path}")
#--------------------------------------

# Function to record video from the webcam
def record_video(camera_index=0, total_frames=30, duration=3):
    """
    Records a video from the specified camera index.
    
    Parameters:
        camera_index (int): Index of the camera to use (default is 0 for PC webcam).
        total_frames (int): Total number of frames to capture (default is 30).
        duration (int): Total duration in seconds for video recording (default is 3 seconds).

    Returns:
        frames (list): A list of captured video frames in RGB format.
    """
    # Open the video capture
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print(f"Error: Unable to access the camera at index {camera_index}.")
        return []

    print("Recording video...")
    
    frames = []
    frame_interval = duration / total_frames  # Time interval between frames
    start_time = time.time()

    while len(frames) < total_frames:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Unable to read frame from the camera.")
            break

        current_time = time.time() - start_time
        if current_time >= len(frames) * frame_interval:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            frames.append(frame_rgb)

    cap.release()
    print("Video recording completed.")
    return frames

# Function to load frames from a manually uploaded video file
def load_video_frames_manual(video_path, total_frames=30):
    """
    Loads frames from a manually provided video file.

    Parameters:
        video_path (str): Path to the video file (manually uploaded).
        total_frames (int): Number of frames to extract.

    Returns:
        frames (list): A list of frames extracted from the video.
    """
    cap = cv2.VideoCapture(video_path)
    frames = []

    if not cap.isOpened():
        print(f"Error: Unable to open video file {video_path}")
        return frames

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(1, frame_count // total_frames)  # Interval for frame extraction

    for i in range(total_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        frames.append(frame_rgb)

    cap.release()
    return frames
# Function to display frames in a 6x5 grid
def display_frames_in_grid(frames):
    """
    Displays video frames in a grid format with 6 rows and 5 columns.

    Parameters:
        frames (list): A list of video frames to display.
    """
    # Set up the grid: 6 rows, 5 columns
    rows, cols = 6, 5
    fig, axes = plt.subplots(rows, cols, figsize=(15, 10))

    # Display frames in the grid
    for i, ax in enumerate(axes.flat):
        if i < len(frames):
            ax.imshow(frames[i])  # Show the frame
            ax.set_title(f"Frame {i+1}")
            ax.axis("off")  # Hide axes
        else:
            ax.axis("off")  # Hide empty axes

    # Make the layout more compact
    plt.tight_layout()
    plt.show()

# Function to preprocess a single frame (normalize and resize)
def preprocess_frame(frame):
    """
    Preprocesses a single video frame by normalizing pixel values and resizing the frame.

    Parameters:
        frame (numpy array): A single video frame to preprocess.

    Returns:
        numpy array: The preprocessed frame with normalized values and resized dimensions (64x64).
    """
    frame_normalized = frame / 255.0  # Normalize the frame
    frame_resized = cv2.resize(frame_normalized, (64, 64))  # Resize to 64x64
    return frame_resized

# Function to convert frames into a numpy array
def convert_frames_to_array(frames):
    """
    Converts a list of video frames into a numpy array after preprocessing each frame.

    Parameters:
        frames (list): A list of video frames.

    Returns:
        numpy array: An array of preprocessed frames.
    """
    # Preprocess each frame
    frames_array = np.array([preprocess_frame(frame) for frame in frames])
    return frames_array

# Function to compare an original frame with its preprocessed version
def compare_frames(frames, frames_preprocessed):
    """
    Compares a specific frame (e.g., frame 15) before and after preprocessing.

    Parameters:
        frames (list): Original video frames.
        frames_preprocessed (numpy array): Preprocessed video frames.
    """
    # Select frame 15 (index 14 as indexing starts at 0)
    frame_15 = frames[14]

    # Select the corresponding preprocessed frame
    frame_15_preprocessed = frames_preprocessed[15]

    # Display the comparison side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Show the original frame
    axes[0].imshow(frame_15)
    axes[0].set_title("Original Frame Example")
    axes[0].axis("off")

    # Show the preprocessed frame
    axes[1].imshow(frame_15_preprocessed)
    axes[1].set_title("Pre-Processed Frame Example")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()

# Function to load a pre-trained LRCN model (from scratch)
def load_net_scratch():
    """
    Loads a pre-trained LRCN model trained from scratch.

    Returns:
        keras.Model: The loaded model.
    """
    model = load_model('lrcn4/lrcn4.keras')  # Ensure the model path is correct
    if model is None:
        print("Error loading model from scratch!")
    return model

# Function to load a pre-trained LRCN model (transfer learning)
def load_net_transfer():
    """
    Loads a pre-trained LRCN model trained using transfer learning.

    Returns:
        keras.Model: The loaded model.
    """
    model = load_model('model_tl/model_tl.keras')  # Ensure the model path is correct
    if model is None:
        print("Error loading transfer learning model!")
    return model

def compare_classifications(frames_array, load_net_scratch, load_net_transfer):
    """
    Compare predictions from scratch-trained and transfer-learning models,
    and display their results side by side in a 1x2 grid.

    Parameters:
        frames_array: Array of preprocessed video frames.
        load_net_scratch: Function to load the scratch-trained model.
        load_net_transfer: Function to load the transfer learning model.
    """
    # Load models
    model_scratch = load_net_scratch()
    model_transfer = load_net_transfer()

    # Make predictions
    prediction_scratch = model_scratch.predict(np.expand_dims(frames_array, axis=0))
    prediction_transfer = model_transfer.predict(np.expand_dims(frames_array, axis=0))

    # Class dictionary
    class_dict = {
        0: 'Left Swipe',
        1: 'Right Swipe',
        2: 'Stop',
        3: 'Thumbs Down',
        4: 'Thumbs Up'
    }

    # Create a 1x2 subplot
    fig, axes = plt.subplots(1, 2, figsize=(18, 8))  # Increase figsize for better visualization

    # Plot for scratch-trained model
    axes[0].barh(list(class_dict.values()), prediction_scratch[0], color='#9DD9F7')
    axes[0].set_title("Scratch-trained Model")
    axes[0].set_xlabel("Probability")
    axes[0].set_ylabel("Class")
    for i, v in enumerate(prediction_scratch[0]):
        axes[0].text(v + 0.02, i, f"{v:.2f}", va='center')

    # Plot for transfer-learning model
    axes[1].barh(list(class_dict.values()), prediction_transfer[0], color='#0085CA')
    axes[1].set_title("Transfer-learning Model")
    axes[1].set_xlabel("Probability")
    axes[1].set_ylabel("Class")
    for i, v in enumerate(prediction_transfer[0]):
        axes[1].text(v + 0.02, i, f"{v:.2f}", va='center')

    # Adjust layout
    plt.tight_layout()
    plt.show()

    # Print predictions
    predicted_class_scratch = class_dict[np.argmax(prediction_scratch)]
    probability_scratch = prediction_scratch.max()
    print(f"Scratch-trained Model: Predicted Class: {predicted_class_scratch}, Probability: {probability_scratch:.4f}")

    predicted_class_transfer = class_dict[np.argmax(prediction_transfer)]
    probability_transfer = prediction_transfer.max()
    print(f"Transfer-learning Model: Predicted Class: {predicted_class_transfer}, Probability: {probability_transfer:.4f}")