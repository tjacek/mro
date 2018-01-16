import numpy as np
import gen,gen.dists
import cluster
import cluster.quality
import cluster.cls_init as cls_init
import visualization

class ClusterExperiment(object):
    def __init__(self,cls_alg,cls_quality):
        self.cls_gen=get_cluster_generator()
        self.cls_alg=cls_alg
        self.cls_quality=cls_quality

    def __call__(self,n_iters=500,n_points=500):
        basic_data=self.cls_gen(n_points)
        cls_alg.start(basic_data)
        for i in range(n_iters):
            cls_alg()
        clustering=cls_alg.get_clustering()
        print(self.cls_quality(clustering))
        cls_data=cls_alg.get_result()
        visualization.show(cls_data,legend=False)

def get_cluster_generator(sigma=0.3,n=3,step=5.0):
    x=[ (i+1)*step for i in xrange(n) ]
    mu=[ (x_i,x_j)  
         for x_i in x
    	    for x_j in x]
    dists=[gen.dists.NormalDist(sigma=sigma,mu=mu_i)
            for mu_i in  mu]
    clust_gen=gen.dists.CompositeDist(dists)
    return  gen.GenerateDataset(clust_gen)

cls_alg=cluster.KMeans(cls_init.kmeans_plus)
cls_exp=ClusterExperiment(cls_alg, cluster.quality.DBI_quality)
cls_exp()