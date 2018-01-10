import numpy as np
import gen,gen.dists

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
data=clust_gen(500)
#print(data.dim)
data.show()