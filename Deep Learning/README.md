
# 🍝 Guess the Pasta: Exploring and Classifying Pasta Varieties using Deep Learning

## Overview

**Guess the Pasta** is an image classification project focused on identifying different **types of pasta** using deep learning. Leveraging convolutional neural networks (CNNs), this project aims to **categorize pasta** into four major classes — **short pasta**, **long pasta**, **filled pasta**, and **lasagna**. The initiative showcases the application of computer vision in food-tech domains such as industrial automation and smart culinary systems.

This project highlights the potential of AI to recognize intricate food shapes and packaging variations, addressing challenges such as visual occlusion and quality inconsistencies in real-world datasets.


## Goals

* Design and train a CNN-based classifier for pasta type recognition.
* Analyze challenges in image-based food classification (e.g., occlusion, shape deformation).
* Explore potential applications in:

  * **Industrial Automation** (automated sorting/packaging of pasta).
  * **Culinary Businesses** (menu optimization, smart inventory systems).


## Dataset Description

The dataset contains labeled images of pasta in four categories:

| Class        | Description                               |
| ------------ | ----------------------------------------- |
| Short Pasta  | Includes penne, farfalle, fusilli, etc.   |
| Long Pasta   | Includes spaghetti, linguine, tagliatelle |
| Filled Pasta | Includes ravioli, tortellini, agnolotti   |
| Lasagna      | Layered pasta sheets, often in dishes     |

Challenges encountered in the dataset include:

* **Occlusion by condiments** in cooked dishes.
* **Packaging coverage** that hides pasta shapes.
* **Shape deformation** (e.g., long pasta bending or clumping when cooked).
* **Inconsistent image dimensions** and **varying quality** due to user-submitted content.


## Methodology

* **Model Architecture:**

  * Implemented a Convolutional Neural Network (CNN) using TensorFlow/Keras.
  * Preprocessing included resizing, normalization, and optional data augmentation (e.g., flips, rotations).

* **Training Strategy:**

  * Supervised learning with categorical cross-entropy loss.
  * Early stopping and validation set monitoring for generalization.

* **Evaluation Metrics:**

  * Accuracy, precision, recall, F1-score per class.
  * Confusion matrix for insight into misclassifications.



## Key Findings

* The model performs well overall but **struggles with long pasta**, likely due to:

  * Shape variability (raw vs. cooked).
  * Occlusion from condiments and sauces.
* **Packaging** significantly impairs recognition accuracy, particularly when brand labels or reflective plastic obscure visual features.
* Lasagna and filled pasta classes were relatively easier to classify due to their distinct shapes.



## Possible Improvements

* **Increase dataset size** to improve generalization and reduce overfitting.
* **Standardize image dimensions** and **improve quality** to aid in feature extraction.
* **Use segmentation models** or object detection to isolate pasta from background and occlusions.
* Integrate **multi-view learning** or **contextual cues** (e.g., cooking tools, serving style) for ambiguous cases.


## Dependencies

To run the project, ensure Python 3.8+ and install the following:
Great! Based on your updated list of dependencies and the use of **TensorFlow/Keras**, here’s an updated version of the **Dependencies** and **Methodology** sections in the `README.md` to reflect **exactly** the libraries you’re using:

---

## Methodology

* **Model Architecture:**

  * Built using **TensorFlow 2 / Keras Sequential API**.
  * Used convolutional layers for feature extraction and dense layers for classification.
  * Applied dropout for regularization and softmax activation for multi-class classification.

* **Preprocessing:**

  * Images were resized and normalized.
  * Data augmentation was applied via `ImageDataGenerator` to simulate real-world variation and prevent overfitting.

* **Training Strategy:**

  * Random seed fixed for full reproducibility: `numpy`, `python`, and `tensorflow` seeds set to 0.
  * Trained with categorical cross-entropy loss and Adam optimizer.
  * Performance tracked on a validation split; early stopping and learning rate reduction optionally applied.

* **Evaluation:**

  * Metrics included accuracy, precision, recall, and F1-score using `classification_report` from `sklearn`.
  * Confusion matrices were visualized using `seaborn` heatmaps.
  * Plots generated with `matplotlib` to visualize accuracy/loss curves and class-wise performance.


## Dependencies

Ensure Python 3.8+ and install the following libraries:


* `tensorflow` — Model architecture, training, and inference
* `keras` — Image preprocessing and model layers
* `numpy` — Numerical operations
* `random` — Python built-in randomness control
* `zipfile`, `shutil`, `time` — File handling and timing

### 📊 Visualization & Evaluation

* `matplotlib` — Loss and accuracy plotting
* `seaborn` — Confusion matrix heatmaps
* `scikit-learn` — Classification report and metrics






## Citation

If you use this project in your research or work, please cite as:

> F. Del Giudice, G.Righetti. (2024). *Guess the Pasta: Exploring and Classifying Pasta Varieties using Deep Learning.*



