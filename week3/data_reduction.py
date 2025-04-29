# PCA Example
from sklearn.decomposition import PCA

# Create PCA object with desired components
pca = PCA(n_components=2)

# Fit and transform data
reduced_data = pca.fit_transform(scaled_data)

# Feature selection using correlation
import pandas as pd
import numpy as np

# Calculate correlation matrix
corr_matrix = df.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find features with correlation greater than 0.8
to_drop = [column for column in upper.columns if any(upper[column] > 0.8)]
