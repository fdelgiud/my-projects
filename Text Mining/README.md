
# 🎬 Exploring Genre Similarities and Enhancing Movie Recommendations

### *A Clustering and Topic Modeling Approach using the TMDb Dataset*

![Movie Dataset Overview](https://pbs.twimg.com/profile_images/1243623122089041920/gVZIvphd_400x400.jpg)


## Overview

This project explores the **semantic and genre-based relationships among movies** using advanced **clustering** and **topic modeling techniques**. Leveraging data from **The Movie Database (TMDb)**, we aim to better understand **latent genre groupings** and improve the **quality of movie recommendations**.

By analyzing:

* Metadata (e.g., genres, keywords)
* Natural language overviews of movies
* Embedded topic distributions

we investigate whether combining **unsupervised learning** with **text modeling** leads to more meaningful **recommendation systems** than traditional similarity-based approaches.


## Goals

* Apply **clustering techniques** to detect **hidden genre structures** beyond conventional classifications.
* Use **topic modeling** to extract **semantic themes** from movie overviews and keywords.
* Build a **hybrid movie recommender** that combines **genre proximity** and **thematic similarity**.


## Methodology

### 📁 Data Source

* **TMDb Movies Dataset**
  Source: [Kaggle Dataset – TMDb Movies (2023)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/data)
  Includes metadata for over **1.4 million movies**, updated daily.

* **Data version used in this project**:
  `movie_plots.csv` (January 4, 2025) – available in the **"Dataset"** folder.

### 🧠 Analytical Techniques

* **Clustering Methods**:

  * K-Means
  * Hierarchical Clustering (SciPy)
  * Fuzzy C-Means (via `scikit-fuzzy`)

* **Dimensionality Reduction & Visualization**:

  * t-SNE
  * Cosine similarity graphs
  * Modularity analysis via NetworkX

* **Topic Modeling**:

  * Latent Dirichlet Allocation (LDA) using `gensim`
  * Text preprocessing with `spaCy`
  * Semantic embeddings using `sentence-transformers`

* **Recommendation Evaluation**:

  * Comparison of basic overview-similarity vs. topic-enhanced similarity
  * WordClouds for topic interpretability


## Key Findings

* Clustering genres reveals **non-obvious genre groupings**, e.g. Sci-Fi and Thriller often cluster together due to shared narrative elements.
* **Topic modeling** successfully extracts dominant themes such as war, love, or space exploration.
* Recommender systems based on **topic-enhanced cosine similarity** outperform vanilla similarity models in thematic consistency.
* Graph-based community detection suggests **clusters of semantically linked movies**, regardless of traditional genre tags.


## Dependencies

To replicate this project, ensure Python 3.8+ and install the following libraries:

### 📊 Data Manipulation

* `pandas` – For structured data operations
* `numpy` – Numerical computation and array handling
* `os`, `shutil`, `re` – File operations and text processing

### 📈 Visualization

* `matplotlib`, `seaborn` – Plotting and statistical graphics
* `wordcloud` – Term visualization
* `networkx` – Graph-based clustering and community detection

### 🧠 Machine Learning & NLP

* `scikit-learn` – KMeans, t-SNE, evaluation metrics

* `scipy` – Hierarchical clustering and distance metrics

* `skfuzzy` – Fuzzy clustering (fuzzy c-means)
  *📌 Install with:* `pip install -U scikit-fuzzy`

* `sentence-transformers` – Semantic embedding of movie overviews

* `gensim` – Topic modeling via LDA and coherence evaluation

* `spaCy` – Natural language preprocessing

### 🌐 Data Access

* `kagglehub` – Download datasets from Kaggle directly


## Citation

If you use this project or build upon it, please cite:

> F. Del Giudice, S. Nava, G. Saresini. (2025).
> *Exploring genre similarities and enhancing movie recommendation through clustering and topic modeling.*


## License

This project is licensed under the **MIT License**.
You are free to use, adapt, and share the code and methods for academic or non-commercial purposes.


