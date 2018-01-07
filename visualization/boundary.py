import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def decision_boundary(dataset,clf,h=0.02):
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    
    X=np.array(dataset.X)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z=clf(np.c_[xx.ravel(), yy.ravel()],single=False)
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.scatter(X[:, 0], X[:, 1], c=dataset.y, cmap=cmap_bold,
                edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()

def show_axis(dataset,eigenvectors,eigenvalues):
    if(dataset.dim!=2):
        raise Exception("Too many dims %d" % dataset.dim)
    
    fig, ax = plt.subplots()
    for label_j in dataset.labels():
        x_0,x_1=dataset.get_cat(label_j)
        ax.scatter(x_0,x_1,label=label_j)    
    
    center=np.array([0.0,0.0])
    for axis_i,eigenvalue_i in zip(eigenvectors,eigenvalues):    
        start, end = center, center + eigenvalue_i * axis_i
        ax.annotate(
            '', xy=end, xycoords='data',
            xytext=start, textcoords='data',
            arrowprops=dict(facecolor='red', width=2.0))
    ax.set_aspect('equal')
    plt.show()