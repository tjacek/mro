import numpy as np 
import gen,gen.dists,gen.conic,utils
import pca,visualization

def pca_exp(n,dim):
    sphere_gen=make_sphere_gen(dim)
    corners=utils.all_seq(dim,[-1,1])
    dataset=sphere_gen(n)
    dataset.add_cat(corners,2)
    red_dataset=pca.transform_pca(dataset)
    visualization.show(red_dataset)

def make_sphere_gen(dim):
    start=[ -1.0 for i in range(dim)]
    dist=gen.dists.UniformDist(start ,width=2.0)	
    preds=[gen.conic.Radius()]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

pca_exp(500,7)