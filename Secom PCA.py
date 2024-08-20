import numpy as np

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            data.append([float(x) if x != 'NaN' else np.nan for x in values])
    return np.array(data)

def replace_nan_with_mean(data):
    col_means = np.nanmean(data, axis=0)
    inds = np.where(np.isnan(data))
    data[inds] = np.take(col_means, inds[1])
    return data

def pca(data, variance_threshold=0.99):
    # Centering the data here
    data_meaned = data - np.mean(data, axis=0)

    # Cov matrix eigenvalues and eigenvectors
    covariance_matrix = np.cov(data_meaned, rowvar=False)
    eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

    # Sorting values
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalues = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:, sorted_index]

    # Calculating the percentage of variance
    eigval_sum = np.sum(sorted_eigenvalues)
    var_explained = [(i / eigval_sum) * 100 for i in sorted_eigenvalues]

    # Calculating the cumulative sum of eigenvalues
    cumulative_var_explained = np.cumsum(var_explained)
    num_components = np.where(cumulative_var_explained > variance_threshold * 100)[0][0] + 1
    table = []
    for i, (variance, cumulative) in enumerate(zip(var_explained, cumulative_var_explained), start=1):
        table.append((i, variance, cumulative))

    return num_components, table, sorted_eigenvectors[:, :num_components]

# load and preprocess the data perform PCA
file_path = "C:/Users/andry/Desktop/492/Assignment 4/secom.txt"  # Replace path if needed
data = load_data(file_path)
data = replace_nan_with_mean(data)
num_components, table_to_fill, principal_components = pca(data)

# prints
print(f"Number of principal components to retain 99% variance: {num_components}")
for row in table_to_fill:
    print(f"Principal Component {row[0]}: {row[1]:.2f}% variance, {row[2]:.2f}% cumulative variance")
