import numpy as np
import gen,gen.dists
import cluster
import visualization

def get_cluster_generator(sigma=0.5,n=3,step=5.0):
    x=[ (i+1)*step for i in xrange(n) ]
    mu=[ (x_i,x_j)  
         for x_i in x
    	    for x_j in x]
    dists=[gen.dists.NormalDist(sigma=sigma,mu=mu_i)
            for mu_i in  mu]
    clust_gen=gen.dists.CompositeDist(dists)
    return  gen.GenerateDataset(clust_gen)

clust_gen=get_cluster_generator()
basic_data=clust_gen(500)
cls_alg=cluster.KMeans(cluster.uniform_init)
cls_alg.start(basic_data)
for i in range(100):
    cls_alg()
cls_data=cls_alg.get_result()
visualization.show(cls_data,legend=False)