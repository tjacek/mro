import scipy.io as sio
import numpy as np 

class Knn(object):
    def __init__(self,metric,k):
        self.metric=metric
        self.k=k
	
    def knn(new,vectors):
        distance=[self.metric(new_x,x_i) 
              for x_i in train_dataset['x']]
        distance=np.array(distance)
        dist_inds=distance.argsort()[0:self.k]
        y=   train_dataset['y']
        nearest=[y[i] for i in dist_inds]
        return nearest

def read_mat(name,flat=False):
    mat_contents = sio.loadmat(name)
    mat_array=mat_contents['a']
    if(flat):
        return mat_array.flatten()
    else:
        return mat_array

if __name__ == "__main__":
    read_mat(name)