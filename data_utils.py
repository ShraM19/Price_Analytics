import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

# Make predictions for future prices (example)
future_timestamps = np.array([timestamp for timestamp in range(100, 110)]).reshape(-1, 1)
future_prices = model.predict(future_timestamps)

print("Predicted future prices:", future_prices)