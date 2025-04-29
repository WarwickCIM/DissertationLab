# Standardization example
from sklearn.preprocessing import StandardScaler

# Create a scaler object
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(numerical_data)

# One-hot encoding for categorical variables
import pandas as pd

# Create dummy variables
one_hot_encoded = pd.get_dummies(categorical_column)
