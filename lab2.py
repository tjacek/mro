import numpy as np 
import gen,gen.dists,gen.conic,gen.spiral,utils
import pca,visualization

def pca_exp(n,dim):
    sphere_gen=make_sphere_gen(dim)
    corners=utils.all_seq(dim,[-1,1])
    dataset=hyper_gen(n)
    dataset.add_cat(corners,2)
    red_dataset=pca.transform_pca(dataset)
    visualization.show(red_dataset)

def make_hyper_gen(dim):
    start=[ -1.0 for i in range(dim)]
    dist=gen.dists.UniformDist(start ,width=2.0)	
    preds=[gen.conic.Radius()]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

def make_spherical_gen():
    dist=gen.dists.NormalDist(sigma=2.0)	
    pred1=gen.conic.SphericalPred([utils.scalar_pred(1.0,True)])
    pred2=gen.conic.SphericalPred([utils.scalar_pred(1.0,False),
		                           utils.scalar_pred(2.0,True)])
    pred3=gen.conic.SphericalPred(r_preds=[utils.scalar_pred(2.0,False)],
    	                          theta_preds=[utils.MultiScalarPred([0,0],[1,1]),
    	                                       utils.MultiScalarPred([-1,-1],[0,0])],
    	                          conj_theta=False)
    preds=[pred1,pred2,pred3]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

#pca_exp(500,7)
#gen=make_spherical_gen()
#dataset=gen(500)
dataset=gen.spiral.make_spiral_dataset(50,4)
visualization.show(dataset)