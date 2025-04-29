library(dplyr)

# Merging datasets
merged_data <- inner_join(left_df, right_df, by = "common_column")
# Other options: left_join, right_join, full_join

# Concatenating datasets
library(tidyr)
concatenated_data <- bind_rows(df1, df2)  # vertically
concatenated_data <- bind_cols(df1, df2)  # horizontally
