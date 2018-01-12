import numpy as np 
import random
import cluster

def uniform_init(points,k):
    points=np.array(points)
    min_p=np.min(points,axis=0)
    max_p=np.max(points,axis=0)
    return [np.random.uniform(min_p,max_p) 
	            for i in range(k)]

def forgy_init(points,k):
    random.shuffle(points)
    return points[0:k]

def partition_init(points,k):
    random_cls=[np.random.randint(k) 
                for point_i in points]
    print(random_cls)
    def cls_helper(i):
        cluster_i=[ point_j
                    for j,point_j in enumerate(points)
                        if random_cls[j]==i]
        return np.array(cluster_i)
    return [ np.mean(cls_helper(i),axis=0)
                for i in range(k)]

def kmeans_plus(points,k):
    n_points=len(points)
    start_index=np.random.randint(n_points)
    means=[points[start_index]]
    indexes=[i for i in range(n_points)]
    def nearest_cluster(point_i):
        print(len(means))
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