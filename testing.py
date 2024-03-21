import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import datetime

# Load data from JSON file
with open('test.json', 'r') as file:
    data = json.load(file)

# Extract timestamps and average prices
timestamps = []
avg_prices = []

for timestamp, info in data.items():
    timestamps.append(info['key'])  # Assuming 'key' is the numerical representation of the timestamp
    avg_prices.append(info['avg_price_in_cents'])

# Convert timestamps into a 2D array
X = np.array(timestamps).reshape(-1, 1)

# Convert average prices into a 1D array
y = np.array(avg_prices)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Function to predict price for a specific date
def predict_price_for_date(date):
    # Convert date to timestamp
    timestamp = int(date.timestamp())
    # Predict price using the model
    predicted_price = model.predict(np.array([[timestamp]]))
    return predicted_price

# Example: Predict price for August 19, 2025
input_date = datetime.datetime(2025, 8, 19)
predicted_price = predict_price_for_date(input_date)

print("Predicted price for", input_date.strftime('%Y-%m-%d'), ":", predicted_price)
