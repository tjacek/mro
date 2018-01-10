import numpy as np
import gen,gen.dists
import cluster
import visualization

def cluster_experiment(init,n_iters=100,n_points=500):
    clust_gen=get_cluster_generator()
    basic_data=clust_gen(n_points)
    cls_alg=cluster.KMeans(init)
    cls_alg.start(basic_data)
    for i in range(n_iters):
        cls_alg()
    cls_data=cls_alg.get_result()
    visualization.show(cls_data,legend=False)

def get_cluster_generator(sigma=0.5,n=3,step=5.0):
    x=[ (i+1)*step for i in xrange(n) ]
    mu=[ (x_i,x_j)  
         for x_i in x
    	    for x_j in x]
    dists=[gen.dists.NormalDist(sigma=sigma,mu=mu_i)
            for mu_i in  mu]
    clust_gen=gen.dists.CompositeDist(dists)
    return  gen.GenerateDataset(clust_gen)


cluster_experiment(init=cluster.uniform_init)