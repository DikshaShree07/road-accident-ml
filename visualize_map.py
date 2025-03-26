import pandas as pd
import folium

# Load clustered accident data
df = pd.read_csv("clustered_accident_data.csv")

# Define cluster colors
cluster_colors = {0: 'blue', 1: 'red', 2: 'green', 3: 'purple', 4: 'orange'}

# Define severity colors & sizes
severity_colors = {1: 'green', 2: 'orange', 3: 'red'}
severity_sizes = {1: 4, 2: 6, 3: 8}

# Create map centered at average location
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=12)

# Add accident points to map
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=severity_sizes[row['Severity']],  # Size based on severity
        color=cluster_colors[int(row['Cluster'])],  # Cluster-based color
        fill=True,
        fill_color=severity_colors[row['Severity']],  # Severity-based color
        fill_opacity=0.6,
        tooltip=f"Time: {row['Time']}<br>Severity: {row['Severity']}<br>Cluster: {row['Cluster']}"  # Shows time on hover
    ).add_to(m)

# Save map
m.save("accident_hotspots.html")
print("Map updated with time tooltips! Open accident_hotspots.html to view.")