import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('your_data.csv')

# Basic data exploration
print(df.info())
print(df.describe())

# Handling missing values
df.fillna(df.mean(), inplace=True)  # Fill with mean
df.dropna(inplace=True)  # Or drop missing values

# Filter data
filtered_df = df[df['column'] > value]

# Group by and aggregate
grouped = df.groupby('category').agg({
    'numeric_col1': 'mean',
    'numeric_col2': ['min', 'max', 'std']
})
