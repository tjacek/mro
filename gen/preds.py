import numpy as np
import gen.triangle

class SimpleNonConvex(object):
    def __init__(self,p1,p2,p3,p4):
        self.triangle1=gen.triangle.InTriangle(p1,p2,p3)
        self.triangle2=gen.triangle.InTriangle(p1,p2,p4)

    def __call__(self,p_n):
        return ((not self.triangle1(p_n)) and  self.triangle2(p_n))

class ElipticCurve(object):
    def __init__(self,a=1.0,b=1.0):
        self.a=a
        self.b=b

    def __call__(self,p):
        return p[1]**2 > (p[0]**3+self.a*p[0]+self.b)

class ReflectedTriangles(object):
    def __init__(self, p1,p2,p3):#,p4,p5):
        self.triangle1=gen.triangle.InTriangle(p1,p2,p3)
        p4=[p1[0],-p1[1]]
        p5=[p3[0],-p3[1]]
        self.triangle2=gen.triangle.InTriangle(p4,p2,p5)

    def __call__(self,p_n):
        return (self.triangle1(p_n) or self.triangle2(p_n))