import numpy as np 

class Knn(object):
    def __init__(self,metric,k):
        self.metric=metric
        self.k=k
	
    def knn(new,vectors):
        k_metric=[ self.metric(new_vec_i)
    	           for vec_i in vectors]
        