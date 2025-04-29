# PCA Example
# Perform PCA
pca_result <- prcomp(scaled_data, center = TRUE, scale. = TRUE)

# Extract principal components
reduced_data <- pca_result$x[, 1:2]

# Feature selection using correlation
library(caret)

# Calculate correlation matrix
correlation_matrix <- cor(numerical_data)

# Find highly correlated features
high_correlation <- findCorrelation(correlation_matrix, cutoff = 0.8)
features_to_remove <- names(numerical_data)[high_correlation]
