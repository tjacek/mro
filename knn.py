import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

class KNN(object):
    def __init__(self,k=1):
        self.k=k
        self.clf = neighbors.KNeighborsClassifier(k)

    def train(self,dataset):
        self.clf.fit(dataset.X,dataset.y)

    def __call__(self,sample):
        pred=self.clf.predict(sample)#np.c_[xx.ravel(), yy.ravel()])
        print(type(pred))
        print(pred)
        return pred[0]

def decision_boundary(dataset,clf,h=0.02):
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    
    X=np.array(dataset.X)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z=clf.predict(np.c_[xx.ravel(), yy.ravel()])
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

#h = .02  # step size in the mesh

# Create color maps
#cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
#cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

#for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    #clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    #clf.fit(X, y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
#    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
#    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
#    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                         np.arange(y_min, y_max, h))
#    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
#    Z = Z.reshape(xx.shape)
#    plt.figure()
#    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
#    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
#                edgecolor='k', s=20)
#    plt.xlim(xx.min(), xx.max())
#    plt.ylim(yy.min(), yy.max())
#    plt.title("3-Class classification (k = %i, weights = '%s')"
#              % (n_neighbors, weights))

#plt.show()
