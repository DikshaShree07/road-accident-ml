import pandas as pd
import numpy as np

# Generate random accident data
num_accidents = 100  # Adjust as needed

# Generate random latitudes & longitudes (Example: New Delhi region)
latitudes = np.random.uniform(28.40, 28.90, num_accidents)
longitudes = np.random.uniform(76.80, 77.30, num_accidents)

# Generate accident severity (1 = Low, 2 = Medium, 3 = High)
severity = np.random.choice([1, 2, 3], size=num_accidents, p=[0.6, 0.3, 0.1])

# Generate random accident times (between 00:00 - 23:59)
times = pd.date_range("2025-01-01", periods=num_accidents, freq='T').time

# Create DataFrame
df = pd.DataFrame({
    'Latitude': latitudes,
    'Longitude': longitudes,
    'Severity': severity,
    'Time': np.random.choice(times, num_accidents)
})

# Save to CSV
df.to_csv("accident_data.csv", index=False)
print("Dataset generated: accident_data.csv")
