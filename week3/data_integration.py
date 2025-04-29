import pandas as pd

# Merging datasets
merged_data = pd.merge(
    left_df,
    right_df,
    how='inner',  # 'inner', 'outer', 'left', 'right'
    on='common_column'  # or left_on='col1', right_on='col2'
)

# Concatenating datasets
concatenated_data = pd.concat([df1, df2], axis=0)  # vertically
concatenated_data = pd.concat([df1, df2], axis=1)  # horizontally
