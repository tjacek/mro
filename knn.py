import numpy as np 
from collections import Counter

def euclid(a,b):
    return np.linalg.norm(a-b)

class KNN(object):
    def __init__(self,k=1,metric=euclid):
        self.model=None#train
        self.metric=metric
        self.k=k

    def __call__(self,sample):
        inds=self.distance(sample)
        nearest=self.get_cats(inds)
        count =Counter(nearest)
        pred_cat=count.most_common()[0][0]
        return pred_cat

    def train(self,dataset):
        self.model=dataset

    def get_cats(self,inds):
        return [self.model.y[i] for i in inds ]

    def distance(self,sample,k=None):
        print(len(self.model))
        dists=[ self.metric(sample,train_i) 
                  for train_i in self.model.X]
        dists=np.array(dists)
        dist_inds=dists.argsort()
        if(self.k!=None):
            return dist_inds[0:self.k]	
        return dist_inds
