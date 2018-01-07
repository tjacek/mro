import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def show_scatter(x,y,errors):
    plt.errorbar(x, y, yerr=errors, fmt='o')
    plt.show()

def show(dataset):
    if(dataset.dim==2):
        fig, ax = plt.subplots()
        for label_j in dataset.labels():
            x_0,x_1=dataset.get_cat(label_j)
            ax.scatter(x_0,x_1,label=label_j)
        plt.legend()
        plt.show()
    else:
        raise Exception("Too many dims %d" % dataset.dim)

