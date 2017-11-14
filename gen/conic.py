import numpy as np

class Hiperbola(object):
    def __init__(self,a=1.0,b=1.0):
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

class SphericalPred(object):
    def __init__(self,r_preds,theta_preds=[],conj_r=True,conj_theta=None):
        self.r_preds=r_preds
        self.theta_preds=theta_preds
        self.conj_r=conj_r
        if(not conj_theta is None):
            conj_theta=conj_r
        self.conj_theta=conj_theta

    def __call__(self,p):
        r_p=r(p)
        theta_x=p[0]/r_p
        theta_y=p[1]/r_p
        theta=(theta_x,theta_y)
        r_bool=[ r_pred_i(r_p) 
                 for r_pred_i in self.r_preds]
        theta_bool=[ r_theta_i(theta) 
                     for r_theta_i in self.theta_preds]
        r_unif=unify_bool(r_bool,self.conj_r)
        theta_unif=unify_bool(theta_bool,self.conj_theta)
        return (r_unif and theta_unif)

def unify_bool(bool_list,conjunction):
    if(not bool_list):
        return True
    if(conjunction):
        return all(bool_list)
    else:
        return any(bool_list)

class Radius(object):
    def __init__(self,r=1.0):
        self.r=r

    def __call__(self,p):
        r_p=r(p)
        return r_p<self.r

def r(point):
    return np.sqrt(np.dot(point,point))

