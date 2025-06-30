

# 📍 Audio, Video, and Image-Based Sign Language Processing: Multi-Modal Recognition and Generation

## Overview

This project addresses **sign language processing** through **audio classification**, **video gesture recognition**, and **image generation** of American Sign Language (ASL) gestures. Utilizing deep learning frameworks (`Keras` and `TensorFlow`), the work integrates multiple biometric inputs — audio signals, video sequences, and static images — to build models for **speech command recognition**, **gesture-controlled systems**, and **synthetic ASL image generation**.

The research aims to enhance communication accessibility for the deaf and hard-of-hearing communities by providing robust, real-time recognition and generation tools.



## Goals

* Develop and train models for accurate **audio classification** of spoken command words.
* Design deep learning architectures for **video-based gesture recognition** linked to device control.
* Implement **Generative Adversarial Networks (GANs)** to generate realistic ASL gesture images.
* Deliver interactive demos to validate model performance in practical scenarios.



## Dataset Description

* **Audio Classification:**
  The **Speech Commands Dataset** (approx. 40,000 one-second `.wav` recordings) comprises 30 distinct words, focusing on 20 core commands like digits and basic instructions. It features diverse speakers and background noises to train robust audio recognition models.

* **Video Gesture Recognition:**
  The video dataset contains labeled clips of five hand gestures for TV control, each captured in 30-frame sequences at resolutions of 360×360 or 120×160 pixels. The dataset includes 663 training and 100 testing videos.

* **Image Generation:**
  The **Sign Language MNIST** dataset contains 24 grayscale ASL letter images (28×28 pixels), excluding letters requiring motion (J and Z). The dataset is split into 27,455 training and 7,172 testing samples, with augmented images to enrich training diversity.



## Methodology

* **Audio Classification Models:**
  Trained convolutional neural networks (CNNs) on spectrogram and Mel-Frequency Cepstral Coefficients (MFCC) features, and fine-tuned the pre-trained YAMNet model for feature extraction and classification.

* **Video Gesture Recognition Models:**
  Employed Long-term Recurrent Convolutional Networks (LRCN), combining convolutional layers for spatial encoding with recurrent units for temporal modeling. Both from-scratch and transfer learning approaches were explored.

* **Image Generation Models:**
  Developed both unconditional GAN and conditional GAN (cGAN) architectures. The GAN learns to produce ASL images from random noise, while the cGAN incorporates class labels enabling targeted image synthesis.



## Key Findings

* Audio classification models demonstrate strong performance in recognizing spoken commands under varied acoustic conditions.
* Video-based LRCN models effectively identify five distinct gestures, validating gesture control feasibility.
* GANs produce high-fidelity synthetic ASL images that can augment training datasets and potentially improve recognition models.



## Dependencies

To run the project, ensure Python 3.8+ and install the following libraries:

### 📊 Data Handling and Processing

* numpy — Numerical computing
* pandas — Tabular data manipulation
* librosa — Audio feature extraction

### 🌍 Audio, Video & Image Processing

* tensorflow, keras — Deep learning framework
* tensorflow\_hub — Pretrained model embeddings (YAMNet)
* matplotlib, seaborn — Visualization
* PIL (Pillow) — Image processing
* OpenCV (optional) — Video frame handling

### 🧠 Machine Learning & Deep Learning

* scikit-learn — Metrics and dataset utilities
* statsmodels (optional) — Statistical analysis
* tensorflow\.keras.layers — Neural network building blocks



## Citation

If you use this project, please cite as:

> F. Del Giudice, S.Nava. (2025). *Audio, Video, and Image-Based Sign Language Processing: Multi-Modal Recognition and Generation.*



## License

This project is licensed under the MIT License — free for personal and academic use, including modification and distribution.

