import numpy as np 
import random
import cluster

def uniform_init(points,k):
    return [cluster.random_centroid(points)  for i in range(k)]

def partition_init(points,k):
    init_clusters=cluster.empty_clusters(k)
    for point_i in points:
        cls_i=np.random.randint(k)
        init_clusters[cls_i].append(point_i)
    return [np.mean(cluster_j,axis=0) 
                for cluster_j in init_clusters]   

def forgy_init(points,k):
    random.shuffle(points)
    return points[0:k]

def kmeans_plus(points,k):
    n_points=len(points)
    start_index=np.random.randint(n_points)
    means=[points[start_index]]
    indexes=[i for i in range(n_points)]
    def nearest_cluster(point_i):
        return min([ cluster.L2(point_i-mean_j)**2
                        for mean_j in means])
    def next_mean():
        weights=[ nearest_cluster(point_i) for point_i in points]
    	weights=np.array(weights)/sum(weights)
        mean_index=np.random.choice(indexes, 1, p=weights)
        return points[mean_index]
    for i in range(1,k):
        means.append(next_mean())
    return means