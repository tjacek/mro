import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import metric_learn

class KNN(object):
    def __init__(self,k=1,metric=None):
        self.k=k
        self.clf = neighbors.KNeighborsClassifier(k)
        self.metric=metric
        self.preproc=None

    def train(self,dataset):
        X=np.array(dataset.X)
        if(self.metric=='mahalo'):
            x=np.array(dataset.X)
            conv_matrix=np.cov(x.T)
            self.clf = neighbors.KNeighborsClassifier(self.k,
                                                      metric='mahalanobis',
                                                      metric_params={'V': conv_matrix})
        if(self.metric=='lmnn'):    
            self.preproc=metric_learn.lmnn.LMNN(k=self.k)
            self.preproc.fit(X,dataset.y)
            X=self.preproc.transform(X)
        self.clf.fit(X,dataset.y)

    def __call__(self,sample,single=True):
        if(self.preproc!=None):
            sample=self.preproc.transform(sample)
        pred=self.clf.predict(sample)
        if(single):
            return pred[0]
        else:
            return pred

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
#    plt.title("3-Class classification (k = %i, weights = '%s')"
#              % (n_neighbors, weights))

    plt.show()