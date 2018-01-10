import numpy as np 
import gen

class KMeans(object):
    def __init__(self, init,k=9):
        self.init=init
        self.k=k
        self.points=None
        self.assign=None
        self.means=None
        self.iters=0

    def start(self,dataset):
        self.points=dataset.get_points()
        self.means=self.init(self.points,self.k)
        print("&&&&&&&&&&&&&")
        print(self.means)

    def get_result(self):
        return gen.Dataset(self.points,self.assign)

    def __call__(self):
        self.assign=[ self.get_cluster(point_i)
                        for point_i in self.points]
        self.means=[self.recompute_mean(cls_i)
                        for cls_i in range(self.k)]
        self.iters+=1

    def get_cluster(self,point_i):
        dist=[np.linalg.norm(point_i-mean_j)
                for mean_j in self.means]
        return np.argmin(dist)

    def recompute_mean(self,cls_i):
        cluster=[ point_i
                    for j,point_i in enumerate(self.points)
                        if(self.assign[j]==cls_i)]
        cluster=np.array(cluster)
        return np.mean(cluster)	

def uniform_init(points,k):
    points=np.array(points)
    min_p=np.min(points,axis=0)
    max_p=np.max(points,axis=0)
    return [np.random.uniform(min_p,max_p) 
	            for i in range(k)]