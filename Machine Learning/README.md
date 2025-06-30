# 🚬 *Behind the Smoke: Analysis and Prediction Based on Biometric Data*

## Overview

Understanding and mitigating smoking behavior remains a cornerstone of global public health initiatives. This project explores how **machine learning models** can be used to **predict an individual’s smoking status** based solely on **biometric features** using a **visual analytics workflow implemented in KNIME**.

Through the analysis of physiological and health-related variables, the study demonstrates how certain models — particularly from the **Bayesian family** — perform well even with limited data. The work contributes to the development of **non-invasive, data-driven screening tools** that can assist healthcare professionals in **early risk detection** and **preventive interventions**.


## Goals

* Use **classification models** to predict **smoking status** from biometric features.
* Identify the most effective models using **evaluation metrics** like accuracy and ROC-AUC.
* Evaluate the **risk of overfitting** across multiple dataset partitions.
* Propose recommendations for integrating **contextual factors** in future models.


## Methodology

* **Platform**: All workflows were developed and executed using the **KNIME Analytics Platform**, a visual workflow-based tool ideal for low-code machine learning applications.

* **Data Source**:

  * The dataset includes anonymized biometric and physiological measurements such as **age**, **height**, **weight**, **blood pressure**, **cholesterol**, and **glucose levels**.

* **Modeling Techniques**:

  * Evaluated models include:

    * **Naive Bayes Tree**
    * **Bayes Net**
    * **SMO (Support Vector Machine)**
  * Performance was assessed using **stratified partitioning**, **cross-validation**, and **model evaluation nodes**.


## Key Findings

* **Naive Bayes Tree** and **Bayes Net** classifiers outperformed others, benefiting from their shared **Bayesian probabilistic framework** which handles uncertainty and variable dependencies effectively.
* While **SMO** (SVM) showed promising results, its performance **dropped on certain partitions**, likely due to overfitting when faced with smaller sample sizes.
* **Naive Bayes-based models** were more robust and less prone to overfitting, making them suitable for scenarios with limited data.
* Findings emphasize the need for **contextual variables** — such as socioeconomic and cultural factors — to achieve **more accurate and holistic predictions**.
* Collaboration across **healthcare, data science, and policy domains** is vital for translating model insights into **effective prevention strategies**.


## Dependencies

This project was developed using the **KNIME Analytics Platform**. To replicate or extend the analysis:

* **KNIME Analytics Platform** (version 4.7+ recommended)
* Additional KNIME Extensions:

  * KNIME Machine Learning Extensions (for model building)
  * KNIME Statistics and Data Mining
  * KNIME Visualization nodes


## Citation

If you use or refer to this work, please cite it as:

> *F.Del Giudice, G.Righetti.* (2025). **Behind the Smoke: Analysis and Prediction Based on Biometric Data.**

---

## License

This project is released under the **MIT License** – feel free to use or adapt the workflow and methodology for research or educational purposes.

---

