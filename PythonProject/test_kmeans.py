import unittest
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class TestKMeansClustering(unittest.TestCase):

    def setUp(self):
        # Load and preprocess sample data
        df = pd.read_parquet('yellow_tripdata_2025-01.parquet')
        features = ['trip_distance', 'fare_amount', 'tip_amount', 'total_amount', 'passenger_count']
        df = df[features].dropna()
        df = df[
            (df['trip_distance'] > 0) & (df['trip_distance'] < 50) &
            (df['fare_amount'] > 0) & (df['fare_amount'] < 300) &
            (df['total_amount'] < 400) &
            (df['passenger_count'] > 0) & (df['passenger_count'] <= 6)
        ]
        scaler = StandardScaler()
        self.data = scaler.fit_transform(df)

    def test_kmeans_runs(self):
        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(self.data)
        self.assertEqual(len(set(kmeans.labels_)), 4)

    def test_no_nan_labels(self):
        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(self.data)
        self.assertFalse(pd.isnull(kmeans.labels_).any())

if __name__ == '__main__':
    unittest.main()
