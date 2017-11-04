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

    def __len__(self):
        return len(self.y)

    def select(self,check):
        indexes=[i for i,y_i in enumerate(self.y)
                   if check(i,y_i) ]
        X_s=[ self.X[i] for i in indexes]
        y_s=[ self.y[i] for i in indexes]
        return Dataset(X_s,y_s)

    def labels(self):
        return list(Set(self.y))
    
    def show(self):
    	fig, ax = plt.subplots()
    	for label_j in self.labels():
    	    
    	    x_0,x_1=self.get_cat(label_j)
            ax.scatter(x_0,x_1,label=label_j)
        plt.legend()
        plt.show()

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

class NormalDist(object):
    def __init__(self, sigma=1.0,mu=0.0, dim=2):
        self.mu=mu
        self.sigma=sigma
        self.dim=dim

    def __call__(self,n):
        points= [np.random.normal(self.mu, self.sigma,self.dim)		
         		    for i in range(n)]
        return points

class UniformDist(object):
    def __init__(self, points,a,b=None):
        if(b==None):
            b=a
        self.points=points
        self.sides=[points[0]+a,points[1]+b]

    def __call__(self,n):
        def unif_helper(i): 
            return np.random.uniform(low=self.points[i], high=self.sides[i])                   
        return [ np.array([unif_helper(0),unif_helper(1)])
                  for i in range(n) ]

class GetCat(object):
    def __init__(self,preds):
        self.preds=preds

    def __call__(self,p):
        for i,pred_i in enumerate(self.preds):
            if(pred_i(p)):
                return i
        return len(self.preds)	