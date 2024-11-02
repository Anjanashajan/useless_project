import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the modified dataset with only 4 features
df = pd.read_csv('keralaland_modified.csv')

# Split data into features and target
X = df[['Rainfall_mm', 'Slope_Angle_degrees', 'Humidity_percent', 'Soil_Moisture_percent']]
y = df['Landslide_Occurred']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize RandomForestClassifier and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(model, 'landslide_model.pkl')
print("Model saved as landslide_model.pkl")
