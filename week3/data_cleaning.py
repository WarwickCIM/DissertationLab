# Python: Different ways to handle missing values
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

df = pd.read_csv('data.csv')

# 1. Check missing values
print(df.isnull().sum())

# 2. Delete rows with missing values
df_cleaned = df.dropna()

# 3. Simple imputation
df['numeric_col'] = df['numeric_col'].fillna(df['numeric_col'].mean())
df['categorical_col'] = df['categorical_col'].fillna(df['categorical_col'].mode()[0])

# 4. Create missing indicator
df['numeric_col_missing'] = df['numeric_col'].isnull().astype(int)

# 5. Advanced imputation (KNN)
imputer = KNNImputer(n_neighbors=5)
df_imputed = pd.DataFrame(
    imputer.fit_transform(df[['col1', 'col2', 'col3']]),
    columns=['col1', 'col2', 'col3']
)
