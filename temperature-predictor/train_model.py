import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('temperature.csv')

# Prepare data for model training
X = data[['temperature']]
y = data['humidity']

# Train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to disk
with open('model/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model training complete and saved as 'model/model.pkl'")
