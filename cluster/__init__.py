import numpy as np 
import gen

class Clustering(object):
    def __init__(self,clusters,centroids):
        self.clusters=clusters
        self.centroids=centroids
        print(self.centroids)
    
    def __len__(self):
        return len(self.clusters)

    def scatter(self,i):
        return np.mean([L2(point_j-self.centroids[i])
                        for point_j in self.clusters[i]])
    
    def separation(self,i,j):
        return L2(self.centroids[i] - self.centroids[j])

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

    def get_clustering(self):
        clusters=[self.get_cluster(i)
                    for i in range(self.k)]
        return Clustering(clusters,self.means)
    
    def get_result(self):
        return gen.Dataset(self.points,self.assign)

    def __call__(self):
        self.assign=[ self.assign_cluster(point_i)
                        for point_i in self.points]
        self.means=[self.get_centroid(cls_i)
                        for cls_i in range(self.k)]
        self.iters+=1

    def assign_cluster(self,point_i):
        dist=[L2(point_i-mean_j)
                for mean_j in self.means]
        return np.argmin(dist)

    def get_cluster(self,cls_i):
        return [ point_i
                    for j,point_i in enumerate(self.points)
                        if(self.assign[j]==cls_i)]
        
    def get_centroid(self,cls_i):
        cluster=self.get_cluster(cls_i)
        cluster=np.array(cluster)
        return np.mean(cluster,axis=0)

def L2(point_i):
    return np.linalg.norm(point_i, ord=2)	