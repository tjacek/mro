import numpy as np
import gen,gen.conic,gen.dists
import exp

def out_of_sphere(n=1000):
    def proportion(dim):
        print(dim)
        sphere_gen=get_sphere_generator(dim)
    	sphere_data=sphere_gen(n)
        y=sphere_data.y
    	return np.mean(y)
    return proportion

def cube_distance(n=1000,mean=True):
    def distance_stats(dim):
        cube_gen=get_cube_generator(dim)
        x=cube_gen(n).X
        distances=pairwise_distance(x)
        if(mean):
            return np.mean(distances)
        else:
            return np.std(distances)
    return distance_stats

def get_cube_generator(dim):
    start=[ -0.5 for i in range(dim)]
    dist=gen.dists.UniformDist(start ,width=1.0)
    cube_gen=gen.GenerateDataset(dist)
    return cube_gen

def get_sphere_generator(dim):
    start=[ -1.0 for i in range(dim)]
    dist=gen.dists.UniformDist(start ,width=2.0)    
    preds=[gen.conic.Radius(1.0)]
    sphere_gen=gen.GenerateDataset(dist,preds)
    return sphere_gen

def pairwise_distance(x):
    return [ np.linalg.norm(x_a-x_b)
             for x_a in x
    	         for x_b in x]

def exp1(n_points):
    sphere_fun=out_of_sphere(n_points)
    sphere_exp=exp.StatsExperiment(sphere_fun,start=2,step=2)
    sphere_exp(5)

def exp2a(n_points):
    sphere_fun=cube_distance(n_points,mean=True)
    sphere_exp=exp.StatsExperiment(sphere_fun,start=2,step=4)
    sphere_exp(5)

def exp2b(n_points):
    sphere_fun=cube_distance(n_points,mean=False)
    sphere_exp=exp.StatsExperiment(sphere_fun,start=2,step=5)
    sphere_exp(10)

exp2b(100)