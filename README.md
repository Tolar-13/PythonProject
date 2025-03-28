# Module 4: K-Means Python Application

This is a Python application built for **Module 4 Assignment: K-Means Python Application** . It applies the **K-Means clustering algorithm** to New York City Yellow Taxi data to uncover patterns in ride distances, fares, and rider behaviours.

The project is organised under the folder `PythonProject` and tracked using Git, as shown in the repository structure.

---

## Project Structure

```
PythonProject/
│
├── .gitignore                     # Specifies files to be ignored by Git
├── kmeans_application.py          # Main clustering script
├── test_kmeans.py                 # Unit tests for clustering
├── yellow_tripdata_2025-01.parquet  # Dataset file (local only)
```

---

## Requirements

To install dependencies, run:

```bash
pip install pandas scikit-learn matplotlib seaborn pyarrow
```

---

## How to Run

1. Download the dataset from the official source:

   [yellow_tripdata_2025-01.parquet](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet)

   and place it in the project directory.

2. Run the main script:

```bash
python kmeans_application.py
```

3. Run unit tests with:

```bash
pytest test_kmeans.py
```

---

## Testing

The file `test_kmeans.py` includes unit tests that confirm:
- The clustering process runs successfully
- It returns the expected number of clusters
- No missing or invalid cluster labels are generated

---

## Output

The clustering algorithm generates a scatter plot showing ride groupings based on:

- Trip distance (x-axis)
- Fare amount (y-axis)

This helps identify common ride types such as:
- Short-distance low-fare trips
- Long-distance or airport-style rides
- Flat-rate/shared service patterns

---

## Dataset

**Source:** NYC Taxi TLC Trip Record Data  
**Download link:** [https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet)

> The dataset should be placed locally in the project folder but is not tracked by Git.

---

## Author

*Alade Adetola*  
Module 4 Assignment – K-Means Clustering Application  

