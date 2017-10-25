import numpy as np


class GenerateDataset(object):
    def __init__(self,dist, preds):
        self.dist=dist
        self.get_cat=GetCat(preds)	

    def __call__(self,n):
        X=self.dist(n)
        y=[self.get_cat(point_i)
            for point_i in X]
        return Dataset(X,y)

class Dataset(object):
    def __init__(self,X,y):
        self.X=X
        self.y=y

class NormalDist(object):
    def __init__(self, sigma=1.0,mu=0.0, dim=2):
        self.mu=mu
        self.sigma=sigma
        self.dim=dim

    def __call__(self,n):
        points= [np.random.normal(self.mu, self.sigma,self.dim)		
         		    for i in range(n)]
        return points

class GetCat(object):
    def __init__(self,preds):
        self.preds=preds

    def __call__(self,p):
        for i,pred_i in enumerate(self.preds):
            if(pred_i(p)):
                return i
        return len(self.preds)	