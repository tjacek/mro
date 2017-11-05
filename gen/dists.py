import numpy as np

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