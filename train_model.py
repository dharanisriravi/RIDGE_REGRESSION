
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# Load data
data = pd.read_csv('dataset/electricity_data.csv')

# Encode 'season'
le = LabelEncoder()
data['season'] = le.fit_transform(data['season'])

# Features and target
X = data[['hour', 'temperature', 'appliance_usage', 'season', 'humidity']]
y = data['power_consumption']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge Regression
model = Ridge()
model.fit(X_train, y_train)

# Save model
with open('model/ridge_model.pkl', 'wb') as f:
    pickle.dump(model, f)
