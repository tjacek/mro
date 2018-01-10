import numpy as np 
import gen

class KMeans(object):
    def __init__(self, init,k=9):
        self.init=init
        self.k=k
        self.points=None
        self.clusters=None

    def start(self,dataset):
        self.points=dataset.get_points()
        self.clusters=self.init(self.points,self.k)

    def get_result(self):
        return gen.Dataset(self.points,self.clusters)

#    def __call__(self,iters=1):
        
def uniform_init(points,k):
	n=len(points)
	return [np.random.uniform(k) 
	            for i in range(n)]