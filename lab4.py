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

    def iters_quality(self,n_iters=50,n_points=500,show=True):
        self.__start__(n_points)
        iter_quality=[ self.cls_quality(self.cls_alg()) 
                        for i in range(n_iters)]
        if(show):    
            cls_data=cls_alg.clustering.as_dataset()
            visualization.show(cls_data,legend=False)
        return iter_quality

    def points_quality(self,n_iters=20,n_points=500, n_epochs=3):
        dataset=self.__start__(n_points)
        points=dataset.get_points()
        def epoch_helper(i):
            for j in range(n_iters):
                self.cls_alg()
            points_quality=cluster.quality.SilhouetteQuality(self.cls_alg.clustering)
            return [ points_quality(point_i) for point_i in points]
        return [ epoch_helper(i) 
                    for i in range(n_epochs)]

    def __start__(self,n_points):
        dataset=self.cls_gen(n_points)
        self.cls_alg.start(dataset)
        return dataset

def init_experiment(n_iters=50,n_epochs=5,n_points=100):
    def alg_helper(init_i):
        cls_alg=cluster.KMeans(init_i)
        return ClusterExperiment(cls_alg=cls_alg,cls_quality=cluster.quality.DBI_quality)
    cls_alg={ "uniform":alg_helper(cls_init.uniform_init),
              "forgy":alg_helper(cls_init.forgy_init),
              "partition":alg_helper(cls_init.partition_init),
              "kmeans_plus":alg_helper(cls_init.kmeans_plus)}
    def init_helper(cls_alg_i):
        print(cls_alg_i.cls_alg)
        alg_quality=[ cls_alg_i.iters_quality(n_iters,n_points,show=False)
                        for j in range(n_epochs)]
        alg_quality=np.array(alg_quality)
        return np.mean(alg_quality,axis=0),np.std(alg_quality,axis=0)               
    results={ name_i:init_helper(cls_alg_i)
                for name_i,cls_alg_i in cls_alg.items()}
    visualization.show_dict(results,labels=('number_of_iterations','DB_index'))

def points_experiment(n_iters=50,n_epochs=3,n_points=100):
    cls_exp=ClusterExperiment(cls_alg=cluster.KMeans(cls_init.uniform_init),
                              cls_quality=cluster.quality.DBI_quality)
    points_stats=cls_exp.points_quality(n_iters,n_points, n_epochs)
    for stats_i in points_stats:
        visualization.show_bar(stats_i)

def get_cluster_generator(sigma=0.3,n=3,step=5.0):
    x=[ (i+1)*step for i in xrange(n) ]
    mu=[ (x_i,x_j)  
         for x_i in x
    	    for x_j in x]
    dists=[gen.dists.NormalDist(sigma=sigma,mu=mu_i)
            for mu_i in  mu]
    clust_gen=gen.dists.CompositeDist(dists)
    return gen.GenerateDataset(clust_gen)

points_experiment(n_iters=1,n_epochs=5,n_points=100)
#init_experiment(n_iters=50,n_epochs=5,n_points=500)