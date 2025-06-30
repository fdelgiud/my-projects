# 📍 Social Infrastructure and School Shootings in Smart Cities: A Chicago Case Study (1990–2024)

## Overview

In the evolving landscape of **Smart Cities**, urban safety stands as a core pillar of **inclusive and sustainable development**. This project investigates the relationship between the **presence of social and community-oriented facilities** and the **likelihood of school shootings**, using the city of **Chicago** as a case study spanning from **1990 to 2024**.

By integrating **geospatial data** on:

* School locations
* School shooting incidents
* Nearby social infrastructure (e.g., **parks, libraries, theatres, cafes**)

we explore whether the **built environment** can act as a **protective factor** against violence in educational settings.

---

## Goals

* Analyze spatial correlations between **school shootings** and **social infrastructure**.
* Use **clustering techniques** and **logistic regression** to detect meaningful spatial patterns.
* Support urban planning policies that enhance **community infrastructure** to foster **safer educational environments**.

---

## Methodology

* **Data Sources**:

  * School locations (1990–2024) (e.g., OpenStreetMap)
  * School shooting incident records from the **[K-12 School Shooting Database](https://www.chds.us/ssdb/)**
  * Geolocated data on public amenities (e.g., OpenStreetMap)

* **Analytical Techniques**:

  * **K-Means and DBSCAN clustering** for spatial hotspot analysis
  * **Logistic regression modeling** to assess associations
  * **Geospatial visualization** using Python libraries like `geopandas`, `folium`, and `matplotlib`

---

## Key Findings

* Higher density of social/community-oriented facilities near schools **correlates with fewer shooting incidents**.
* **Clusters** of incidents often appear in areas with **sparse infrastructure** or fewer public engagement spaces.
* Results **do not claim causality** but suggest that **urban design and social infrastructure** may influence safety outcomes.

---

## Dependencies

* Python ≥ 3.8
* geopandas
* pandas
* scikit-learn
* folium
* matplotlib
* seaborn

Install with:

```bash
pip install -r requirements.txt
```

---

## Citation

If you use this work, please cite as:

> "\[F.Del Giudice, C.Mariani]. (2025). * To what extent does the presence of social places reduce the likelihood of a school shooting in Chicago*"

---

## License

This project is licensed under the MIT License. See `LICENSE` for more information.





  


