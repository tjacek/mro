import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def show_scatter(x,y,errors,labels=('x','y')):
    plt.errorbar(x, y, yerr=errors, fmt='o')
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.show()

def show(dataset,legend=True):
    if(dataset.dim==2):
        fig, ax = plt.subplots()
        for label_j in dataset.labels():
            data=dataset.get_cat(label_j)
            x_0=data[:,0]
            x_1=data[:,1]
            ax.scatter(x_0,x_1,label=label_j)
        if(legend):
            plt.legend()
        plt.show()
    else:
        raise Exception("Too many dims %d" % dataset.dim)

