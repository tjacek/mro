import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def show_dict(result_dict,labels=('x','y')):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    for name_i,values_i in result_dict.items():
        y_i=values_i[0]
        x_i=range(len(y_i))
        error_i=values_i[1]
        plt.errorbar(x_i, y_i, yerr=error_i,label=name_i)
    ax.legend(loc='upper center')
    plt.show()

def show_scatter(x,y,errors,labels=('x','y'),plot_title=None):
    plt.errorbar(x, y, yerr=errors, fmt='o')
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    if(plot_title is not None):
        plt.title(plot_title)
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

