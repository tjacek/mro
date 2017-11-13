import numpy as np
from sklearn import decomposition
import gen

def transform_pca(dataset,n=2):
    pca = decomposition.PCA(n_components=n)
    pca.fit(dataset.X)  
    new_X = pca.transform(dataset.X)
    return gen.Dataset(new_X,dataset.y)