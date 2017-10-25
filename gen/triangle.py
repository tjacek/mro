import numpy as np

class InTriangle(object):
    def __init__(self, A,B,C,eps=0.01):
        self.A=A
        self.B=B
        self.C=C
        self.eps=eps

    def __call__(self,P):
        full_area=triangle_area(self.A,self.B,self.C)
        p1_area=triangle_area(P,self.B,self.C)
        p2_area=triangle_area(self.A,P,self.C)		
        p3_area=triangle_area(self.A,self.B,P)		
        diff=full_area-(p1_area+p2_area+p3_area)
        return np.abs(diff)<self.eps 

def triangle_area(a,b,c):
    v1=(a[0]-c[0])*(b[1]-a[1])
    v2=(a[0]-b[0])*(c[1]-a[1])
    return np.abs(v1-v2)/2.0

tri= InTriangle([2.0,0.0],[0.0,1.0],[0.0,-1.0])
print(tri( [1.0,1.0]))
print(tri( [1.0,0.0]))