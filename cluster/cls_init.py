import numpy as np 
import random

def uniform_init(points,k):
    points=np.array(points)
    min_p=np.min(points,axis=0)
    max_p=np.max(points,axis=0)
    return [np.random.uniform(min_p,max_p) 
	            for i in range(k)]

def forgy_init(points,k):
    random.shuffle(points)
    print(points[:k])
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
    	