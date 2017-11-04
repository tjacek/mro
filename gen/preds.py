import numpy as np
import gen.triangle

class SimpleNonConvex(object):
    def __init__(self,p1,p2,p3,p4):
        self.triangle1=gen.triangle.InTriangle(p1,p2,p3)
        self.triangle2=gen.triangle.InTriangle(p1,p2,p4)

    def __call__(self,p_n):
        return (not self.triangle1(p_n)) and  self.triangle2(p_n)

class TwoTriangles(object):
   	def __init__(self, p1,p2,p3,p4,p5):
   	    self.triangle1=gen.triangle.InTriangle(p1,p2,p3)
        self.triangle2=gen.triangle.InTriangle(p3,p4,p5)

class ElipticCurve(object):
    def __init__(self,a,b=1.0):
        self.a=a
        self.b=b

    def __call__(self,p):
        return p[1]**2 > (p[0]**3+self.a*p[0]+self.b)		