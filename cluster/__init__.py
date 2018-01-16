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

    def as_dataset(self):
        points=[]
        y=[]
        for j,cls_j in enumerate(self.clusters):
            for point_i in cls_j:
                points.append(point_i)
                y.append(j)
        return gen.Dataset(points,y)

class KMeans(object):
    def __init__(self, init,k=9):
        self.init=init
        self.k=k
        self.clustering=None

    def start(self,dataset):
        points=dataset.get_points()
        clusters=[dataset.get_cat(i) for i in range(self.k)]
        means=self.init(points,self.k)
        self.clustering=Clustering(clusters,means)

    def __call__(self):
        new_clusters=[[] for i in range(self.k)]
        for cls_j in self.clustering.clusters:
            for point_i in cls_j:
                new_cls=self.assign_cluster(point_i)
                new_clusters[new_cls].append(point_i)
        new_centroids=[ np.mean(cls_i,axis=0)
                        for cls_i in new_clusters]
        self.clustering=Clustering(new_clusters,new_centroids)

    def assign_cluster(self,point_i):
        dist=[L2(point_i-centroid_j)
                for centroid_j in self.clustering.centroids]
        return np.argmin(dist)

def L2(point_i):
    return np.linalg.norm(point_i, ord=2)	