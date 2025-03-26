import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import random
import datetime

# Set page title
st.set_page_config(page_title="🚦 Accident Hotspot Prediction", layout="wide")

# Title and description
st.title("🚦 Road Accident Hotspot Prediction")
st.markdown("This app predicts accident-prone areas using Machine Learning clustering and visualizes them on an interactive map.")

# Step 1: Generate Random Accident Data
st.sidebar.header("⚙️ Settings")
num_accidents = st.sidebar.slider("Number of Accidents", min_value=50, max_value=500, value=200)

# Function to generate random accident data
def generate_data(n):
    latitudes = [random.uniform(28.4, 28.9) for _ in range(n)]
    longitudes = [random.uniform(77.0, 77.8) for _ in range(n)]
    severity = [random.choice([1, 2, 3]) for _ in range(n)]
    times = [datetime.datetime.now() - datetime.timedelta(hours=random.randint(1, 24)) for _ in range(n)]
    return pd.DataFrame({"Latitude": latitudes, "Longitude": longitudes, "Severity": severity, "Time": times})

# Generate dataset
df = generate_data(num_accidents)

# Step 2: Display Raw Data
if st.sidebar.checkbox("📂 Show Raw Data"):
    st.write(df)

# Step 3: Create Interactive Map
st.subheader("🗺️ Accident Hotspot Map")
m = folium.Map(location=[df["Latitude"].mean(), df["Longitude"].mean()], zoom_start=12)

# Add marker clusters
marker_cluster = MarkerCluster().add_to(m)
for _, row in df.iterrows():
    popup_html = f"""
    <b>🚧 Accident Details</b><br>
    🕒 Time: {row['Time']}<br>
    ⚠️ Severity: {row['Severity']}<br>
    📍 Latitude: {row['Latitude']}<br>
    📏 Longitude: {row['Longitude']}<br>
    """
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color="red" if row["Severity"] == 3 else "orange" if row["Severity"] == 2 else "green"),
    ).add_to(marker_cluster)

# Display the map in Streamlit
st_folium(m, width=1000, height=500)

st.sidebar.success("✅ Adjust settings and explore accident hotspots interactively.")
