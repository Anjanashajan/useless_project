import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
data = pd.read_csv('C:/xampp/htdocs/landslide/landslide_data.csv')

# Print column names to debug
print("Columns in the dataset:", data.columns)

# Select relevant features for training the model
# Since we don't have 'Rainfall_mm', 'Slope_Angle_degrees', etc., adjust to use available data
X = data[['landslide_trigger', 'landslide_size']].copy()
y = data['landslide_category']  # Assuming this is your target variable

# Handle missing values (optional)
X.fillna('unknown', inplace=True)  # Fill missing values with a placeholder
y.fillna('unknown', inplace=True)

# Convert categorical columns to numeric using one-hot encoding
X = pd.get_dummies(X, columns=['landslide_trigger', 'landslide_size'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model as a .pkl file
joblib.dump(model, 'landslide_model.pkl')

print("Model trained and saved as 'landslide_model.pkl'")
