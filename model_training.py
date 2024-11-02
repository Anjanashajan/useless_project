import pandas as pd

# Load your dataset
df = pd.read_csv('landslide_data.csv')

# Keep only the required columns for retraining
df = df[['Rainfall_mm', 'Slope_Angle_degrees', 'Humidity_percent', 'Soil_Moisture_percent', 'Landslide_Occurred']]

# Save the modified dataset
df.to_csv('keralaland_modified.csv', index=False)

print("Modified dataset saved successfully.")
