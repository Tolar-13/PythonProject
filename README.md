# Module 4: K-Means Python Application

This project is a Python application developed for **Module 4** of a data science course. It applies the **K-Means clustering algorithm** to analyse New York City Yellow Taxi trip data. The project is organised under the folder name `PythonProject` and includes clean code, unit tests, and a well-structured setup using Git.

---

## 📁 Project Structure

```
PythonProject/
│
├── Kmeans_application.py       # Main clustering script
├── test_kmeans.py              # Unit tests using pytest
├── yellow_tripdata_2025-01.parquet  # NYC Yellow Taxi dataset
├── .gitignore                  # Files/folders excluded from Git tracking
├── .idea/                      # PyCharm IDE settings (optional to track)
├── .git/                       # Git repo metadata
├── README.md                   # Project documentation
└── .venv/                      # Local virtual environment (excluded from Git)
```

---

## 📦 Requirements

Install the required Python libraries using:

```bash
pip install pandas scikit-learn matplotlib seaborn pyarrow
```

---

## 🚀 How to Run

1. Make sure the dataset file (`yellow_tripdata_2025-01.parquet`) is in the same directory as your scripts.
2. Run the clustering application:

```bash
python Kmeans_application.py
```

3. Run unit tests:

```bash
pytest test_kmeans.py
```

---

## 🧪 Testing

`test_kmeans.py` includes tests that verify:
- The clustering process runs without errors
- The number of clusters returned is as expected
- There are no missing or invalid cluster labels

Tests use Python's `unittest` framework and are compatible with `pytest`.

---

## 📊 Output

The clustering script produces a scatter plot showing taxi ride clusters based on:

- Trip distance
- Fare amount

This helps identify trip types such as:
- Short local rides
- Long-distance/high-fare rides (e.g., airport)
- Flat-rate/shared service rides

---

## 🗃️ .gitignore Usage

The `.gitignore` file helps keep the repository clean by ignoring:

```
.venv/
__pycache__/
.idea/
*.parquet
```

> This prevents unnecessary or large files from being committed to the repository.

---

## 📚 Dataset

**Source:** [NYC Taxi TLC Trip Record Data (AWS Open Data)](https://registry.opendata.aws/nyc-tlc-trip-records/)

> ⚠️ The dataset is included locally but excluded from Git to reduce repository size.

---

## 👨‍💻 Author

*Your Name*  
Module 4 Assignment – K-Means Clustering Application  
*Course/Instructor Name (if required)*
