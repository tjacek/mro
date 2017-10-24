import numpy as np 

class KNN(object):
	def __init__(self,samples,cats,metric,k=1):
		self.samples=samples
        self.cats=cats
		self.metric=metric
		self.k=k

    def __call__(self,sample):
    	inds=self.distance(sample)
        nearest=self.get_cats(inds)
        count =Counter(nearest)
        pred_cat=count.most_common()[0][0]
        return pred_cat

    def get_cats(self,inds):
        return [self.cats[i]  for i in inds ]

    def distance(sample,k=None):
        dists=[ self.metric(sample,train_i) 
                  for train_i in self.train]
        dists=np.array(dists)
        dist_inds=distance.argsort()
        if(self.k!=None):
            return dist_inds[0:self.k]	
        return dist_inds