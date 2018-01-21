import numpy as np
import cluster

def DBI_quality(clust):
    n_clust=len(clust)
    def R(i,j):
        return (clust.scatter(i) - clust.scatter(j))/clust.separation(i,j)
    def D(i):
        return max([ R(i,j) 
        	          for j in range(n_clust)
        	              if i!=j])
    return np.mean([ D(i) for i in range(n_clust)])

class SilhouetteQuality(object):
    def __init__(self,clustering):
        self.clustering=clustering

    def __call__(self,point_i,clust_i=None):
        if(clust_i is None):
            clust_i=cluster.assign_cluster(point_i,self.clustering.centroids)
        a_i=self.clustering.avg_distance(point_i,clust_i)
        b_i=min([self.clustering.avg_distance(point_i,clust_j) 
        	        for clust_j in range(len(self.clustering)) 
        	            if clust_j!=clust_i])
        return (b_i -a_i) /max([a_i,b_i])
