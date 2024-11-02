import pandas as pd
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('landslide_data.csv')

# Load the trained model
model = joblib.load('landslide_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

# Function to get features from the dataset based on the location
def get_features(location):
    # Filter the data to find the row for the given location
    feature_row = data[data['Location'] == location]

    if feature_row.empty:
        raise ValueError("Location not found in the dataset.")

    # Extract the necessary features from the row
    rainfall = feature_row['Rainfall_mm'].values[0]
    slope = feature_row['Slope_Angle_degrees'].values[0]
    humidity = feature_row['Humidity_percent'].values[0]
    soil_moisture = feature_row['Soil_Moisture_percent'].values[0]

    # Return the feature values in a list to match model input
    return [rainfall, slope, humidity, soil_moisture]



@app.route('/predict', methods=['POST'])
def predict():
    # Get location input from the form
    location = request.form['location']

    try:
        # Get features based on the input location
        features = get_features(location)
        rainfall, slope, humidity, soil_moisture = features

        # Predict using the model
        prediction = model.predict([features])[0]  # Make sure model expects correct input shape

        # Generate appropriate result based on the prediction
        if prediction == 1:
            result_message = "WARNING: Significant Landslide Risk Detected!"
        else:
            result_message = "All Clear! Minimal Risk of Landslides."

    except ValueError as e:
        # Handle case where location is not found in the dataset
        result_message = str(e)
        rainfall = slope = humidity = soil_moisture = "N/A"

    # Render the results page
    return render_template('result.html', result_message=result_message, location=location,
                           rainfall=rainfall, slope=slope, humidity=humidity, soil_moisture=soil_moisture)
if __name__ == '__main__':
    app.run(debug=True)
