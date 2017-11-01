import numpy as numpy


class Hiperbola(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self,p):
        x=(p[0]/self.a)**2
        y=(p[1]/self.b)**2
        return (x-y) < 1.0

class Ellipse(object):
    def __init__(self,a,b,r=1.0,c=[0.0,0.0]):
        self.a=a
        self.b=b
        self.c=c
        self.r=r

    def __call__(self,p):
        x=(p[0]-self.c[0])/self.a
        y=(p[1]-self.c[1])/self.b
        return (x**2 + y**2) < self.r
