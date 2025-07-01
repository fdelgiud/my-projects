# 🌍 The Role of Internet Freedom in Political Transformations

**Insights from the Arab Spring**

## Overview

**Internet freedom** plays a vital role in shaping modern political dynamics. This project investigates how changes in online freedom correlate with major political transformations — particularly the **Arab Spring**. Using data from **Freedom House's "Freedom on the Net"** survey, we explore patterns and disruptions in digital freedom, and analyze their implications on civic engagement and regime change.

Our central research question:

> *What role does internet freedom play in political changes, particularly during the Arab Spring?*



## Goals

* Analyze temporal and regional trends in internet freedom.
* Identify **anomalies** and correlate them with key political events.
* Use **time-series modeling** and **regression analysis** to uncover underlying patterns.
* Examine case studies — especially the Arab Spring — to contextualize findings.



## Methodology

1. **Exploratory Data Analysis (EDA):**

   * Visualize changes in internet freedom across regions and over time.
   * Analyze specific metrics (obstacles to access, limits on content, violations of rights).

2. **Anomaly Detection:**

   * Detect unusual shifts in internet freedom using time series modeling (ARIMA).
   * Use mathematical modeling to identify points of disruption correlated with political unrest.

3. **Predictive Modeling:**

   * Apply machine learning (e.g., **Support Vector Regression**) to quantify trends.
   * Cross-validate models to assess predictive accuracy.

4. **Case Study: Arab Spring**

   * Zoom in on Tunisia, Egypt, Libya, and Syria.
   * Map disruptions in digital freedom before, during, and after revolutions.
   * Analyze consequences for democratic transition and repression.



## Key Findings

* Significant **drops in internet freedom** occurred during periods of intense political upheaval.
* **Anomalies in digital access** often preceded or coincided with mass mobilizations.
* The Arab Spring highlights both the **empowering role of the internet** and the **state's attempts to control it**.
* Sustaining internet freedom is crucial for **democratic consolidation** and **long-term political stability**.



## Dataset

**Source:** [Freedom on the Net](https://freedomhouse.org/report/freedom-net) by Freedom House

* Covers global data on digital rights, content restrictions, and access barriers.
* Time span: 2009–2021
* Regions of focus: Middle East and North Africa (MENA)



## Dependencies

Ensure Python 3.8+ and install the following packages:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn statsmodels
```

### 📊 Data Analysis & Visualization

* `pandas`, `numpy` — Data manipulation and analysis
* `matplotlib`, `seaborn` — Static visualizations
* `plotly` — Interactive plots and dashboards

### 🧠 Machine Learning & Time Series

* `scikit-learn` — SVR modeling and preprocessing
* `statsmodels` — ARIMA modeling for time series anomaly detection
* `itertools`, `warnings` — Grid search and runtime management



## Citation

If you use or refer to this work, please cite as:

> Francesca Del Giudice, Yasmine Khajjou, Martina Pantò, and Gaia Righetti. (2025).
> *The Role of Internet Freedom in Political Transformations: Insights from the Arab Spring.*



## License

This project is released under the **MIT License** – feel free to use or adapt the workflow and methodology for **research or educational purposes**.



