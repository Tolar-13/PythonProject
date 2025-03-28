# Install dependencies
# pip install pandas scikit-learn matplotlib seaborn pyarrow

# =============================
# NYC Taxi Data Clustering App
# =============================

# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_parquet('yellow_tripdata_2025-01.parquet')

# Select the numerical features relevant to taxi rides
features = ['trip_distance', 'fare_amount', 'tip_amount', 'total_amount', 'passenger_count']
df_cluster = df[features].dropna() # Drop rows with any missing values

# -----------------------------
# Clean the Data (Outlier Removal)
# -----------------------------

# Filter out unrealistic values to improve clustering results
df_cluster = df_cluster[
    (df_cluster['trip_distance'] > 0) & (df_cluster['trip_distance'] < 50) &
    (df_cluster['fare_amount'] > 0) & (df_cluster['fare_amount'] < 300) &
    (df_cluster['total_amount'] < 400) &
    (df_cluster['passenger_count'] > 0) & (df_cluster['passenger_count'] <= 6)
]

# -----------------------------
# Data Scaling for K-Means
# -----------------------------

# Scale the data to standardise features before clustering
scaler = StandardScaler()
scaled = scaler.fit_transform(df_cluster)

# -----------------------------
# Apply K-Means Clustering
# -----------------------------

# Create and fit the K-Means model with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42)
df_cluster['cluster'] = kmeans.fit_predict(scaled)

# -----------------------------
# Visualise the Clusters
# -----------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(
    x=df_cluster['trip_distance'],
    y=df_cluster['fare_amount'],
    hue=df_cluster['cluster'],
    palette='viridis'
)
plt.title('NYC Taxi Trip Clusters (Cleaned Data)')
plt.show()


