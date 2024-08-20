# SECOM PCA Dimensionality Reduction

## Overview

In semiconductor manufacturing, a vast number of sensor signals are monitored to ensure product quality and efficiency. However, not all these signals are critical for predicting manufacturing outcomes. This project leverages Principal Component Analysis (PCA) to reduce the dimensionality of the SECOM dataset, simplifying data analysis while retaining 99% of the variance.

## Data Preprocessing

- **Handling Missing Values**: 
  - The SECOM dataset contains missing values (NaNs), which are replaced with the mean value of their respective feature to create a complete dataset for analysis.

## Principal Component Analysis (PCA)

- **Data Centering**: 
  - The dataset is centered by subtracting the mean of each feature, a crucial step for effective PCA.
  
- **Covariance Matrix and Eigenvalue Decomposition**: 
  - The covariance matrix is computed to understand how features vary together. Eigenvalues and eigenvectors are then derived to determine the principal components.

- **Variance Explained**:
  - PCA calculates the percentage of variance each principal component contributes. Our goal is to retain enough components to cover 99% of the dataset's variance while minimizing complexity.

## Results

- Out of the original 590 features, PCA identified that only 17 principal components are necessary to retain 99% of the variance in the dataset.
- The first principal component alone captures over 59% of the variance, demonstrating its significant influence on the data.

![Screenshot (2217)](https://github.com/user-attachments/assets/ed6b35fc-7d1e-47ab-aa25-4e88eb9ee3f4)

## Conclusion
  - This project effectively demonstrates how PCA can be used to simplify high-dimensional datasets like SECOM, significantly reducing the number of features without sacrificing essential information. The approach provides a clearer, more manageable dataset for further analysis or modeling.
