import numpy as np
from sklearn import decomposition
import gen
import visualization

def transform_pca(dataset,n=2):
    pca = decomposition.PCA(n_components=n)
    pca.fit(dataset.X)  
    new_X = pca.transform(dataset.X)
    return gen.Dataset(new_X,dataset.y)

def transform_kernel(dataset,kernel="rbf", gamma=10,n=2):
    kpca = decomposition.KernelPCA(kernel=kernel, gamma=gamma)
    X_kpca = kpca.fit_transform(np.array(dataset.X)).T
    X_kpca = X_kpca[0:dataset.dim].T
    return gen.Dataset(X_kpca,dataset.y)

def show_pca(dataset):
    pca = decomposition.PCA(n_components=2)
    pca.fit(dataset.X)
    eigenvectors,eigenvalues=pca.components_,pca.explained_variance_ratio_
    visualization.show_axis(dataset,eigenvectors,eigenvalues)