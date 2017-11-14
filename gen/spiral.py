import numpy as np
import gen

def make_spiral_dataset(n,k):
    d_theta=1.0/float(k+1)
    c_point=np.array([0.0,0.0])
    dataset=gen.Dataset([c_point],[0])
    for i in range(k):
        x_i=random_spiral(n,i*d_theta)
        dataset.add_cat(x_i,i)
    return dataset

def random_spiral(n,theta):
    def spiral_helper(theta):
        theta=(2*np.pi*theta)
        x=np.random.uniform(low=-1.0, high=1.0)
        y=np.sin(0.5*np.pi*x)
        new_x=x*np.cos(theta)-y*np.sin(theta)
        new_y=x*np.sin(theta)+y*np.cos(theta)
        return np.array([new_x,new_y])
    return [spiral_helper(theta) for i in range(n)]
