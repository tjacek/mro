import numpy as np
from sklearn import decomposition

def transform_pca(dataset,n=3):
    pca = decomposition.PCA(n_components=n)
    pca.fit(X)  
    dataset.X = pca.transform(dataset.X)
    return dataset