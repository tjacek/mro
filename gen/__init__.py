import numpy as np
from sets import Set
import matplotlib.pyplot as plt

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
        self.dim=X.shape[1]

    def __len__(self):
        return len(self.y)

    def __getitem__(self,i):
        return self.X[i],self.y[i]
    
    def __add__(self,other_dataset):
        self.X=self.X+other_dataset.X
        self.y=self.y+other_dataset.y
        return self

    def add(self,x_i,y):
        self.X.append(x_i)
        self.y.append(y)

    def select(self,check):
        if(type(check)==list):
            check=SetCheck(check)
        indexes=[i for i,y_i in enumerate(self.y)
                   if check(i,y_i) ]
        X_s=[ self.X[i] for i in indexes]
        y_s=[ self.y[i] for i in indexes]
        return Dataset(X_s,y_s)

    def labels(self):
        return list(Set(self.y))
    
    def get_cat(self,cat_i):
    	points=[ point_i 
    	         for i,point_i in enumerate(self.X)
    	           if self.y[i]==cat_i]
        data=np.array(points)
        x_0=data[:,0]
        x_1=data[:,1]
        return x_0,x_1

class Modulo(object):
    def __init__(self,k):
        self.k=k

    def __call__(self,i,y_i):
        return (i % 2)==self.k

class SetCheck(object):
    def __init__(self, array):
        self.index_set = Set(array)

    def __call__(self,i,y_i):
        return (i in self.index_set)
        
class GetCat(object):
    def __init__(self,preds):
        self.preds=preds

    def __call__(self,p):
        for i,pred_i in enumerate(self.preds):
            if(pred_i(p)):
                return i
        return len(self.preds)	