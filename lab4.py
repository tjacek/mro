import numpy as np
import gen.dists

def get_cluster_generator():
    dists=[gen.dists.NormalDist()]
    clust_gen=gen.dists.CompositeDist(dists)
    return clust_gen