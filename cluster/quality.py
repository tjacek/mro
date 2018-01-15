import numpy as np

def DBI_quality(clust):
    n_clust=len(clust)
    def R(i,j):
        return (clust.scatter(i) - clust.scatter(j))/clust.separation(i,j)
    def D(i):
        return max([ R(i,j) 
        	          for j in range(n_clust)
        	              if i!=j])
    return np.mean([ D(i) for i in range(n_clust)])