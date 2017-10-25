import numpy as np

def triangle_area(a,b,c):
    v1=(a[0]-c[0])*(b[1]-a[1])
    v2=(a[0]-b[0])*(c[1]-a[1])
    return np.abs(v1-v2)/2.0

print(triangle_area([2,0],[0,1],[0,-1]))