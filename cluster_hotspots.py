import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("accident_data.csv")

# Select relevant columns (Latitude, Longitude)
X = df[['Latitude', 'Longitude']]

# Apply K-Means clustering (5 clusters)
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X)

# Save clustered data
df.to_csv("clustered_accident_data.csv", index=False)
print(f"Accident data clustered into {num_clusters} hotspots and saved.")
