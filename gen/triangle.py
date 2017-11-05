import numpy as np

class InTriangle(object):
    def __init__(self, A,B,C,eps=0.01):
        self.points=[A,B,C]
        self.eps=eps

    def __call__(self,P):
        A,B,C=self.points[0],self.points[1],self.points[2]
        full_area=triangle_area(A,B,C)
        p1_area=triangle_area(P,B,C)
        p2_area=triangle_area(A,P,C)		
        p3_area=triangle_area(A,B,P)		
        diff=full_area-(p1_area+p2_area+p3_area)
        return np.abs(diff)<self.eps 

    def translate(self,x=None,y=None):
        if(x!=None):
            for point_i in self.points:
                point_i[0]=point_i[0]+x
        if(y!=None):
            for point_i in self.points:
                point_i[1]=point_i[1]+y

def triangle_area(a,b,c):
    v1=(a[0]-c[0])*(b[1]-a[1])
    v2=(a[0]-b[0])*(c[1]-a[1])
    return np.abs(v1-v2)/2.0