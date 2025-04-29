# Standardization example
# Using base R
scaled_data <- scale(numerical_data)

# Using dplyr
library(dplyr)
scaled_data <- numerical_data %>%
  mutate_all(~(.-mean(.))/sd(.))

# One-hot encoding
library(fastDummies)
one_hot_encoded <- dummy_cols(data, select_columns = "categorical_column")
