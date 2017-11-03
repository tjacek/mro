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