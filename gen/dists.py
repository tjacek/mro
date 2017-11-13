import numpy as np

class NormalDist(object):
    def __init__(self, sigma=1.0,mu=0.0, dim=2):
        self.dim=2
        self.mu=mu
        self.sigma=sigma
        self.dim=dim

    def __call__(self,n):
        points= [np.random.normal(self.mu, self.sigma,self.dim)		
         		    for i in range(n)]
        return points

class UniformDist(object):
    def __init__(self, start,width):
        if(type(start)==list):
            start=np.array(start)
        self.dim=start.shape[0]
        if(type(width)==float):
            width=[width for i in range(self.dim) ]
        self.start=start
        self.end=[ start_i+width_i 
                    for start_i,width_i in zip(start,width)]

    def __call__(self,n):
        def unif_helper(i):
            return np.random.uniform(low=self.start[i], high=self.end[i])        
        return [ np.array([unif_helper(i) for i in range(self.dim)])
                   for i in range(n) ]

