import numpy as np
from sklearn import neighbors, datasets
import metric_learn
import gen

class KNN(object):
    def __init__(self,k=1,metric=None):
        self.k=k
        self.clf = neighbors.KNeighborsClassifier(k)
        self.metric=metric
        self.preproc=None

    def train(self,dataset):
        X=np.array(dataset.X)
        if(self.metric=='mahalo'):
            x=np.array(dataset.X)
            conv_matrix=np.cov(x.T)
            self.clf = neighbors.KNeighborsClassifier(self.k,
                                                      metric='mahalanobis',
                                                      metric_params={'V': conv_matrix})
        if(self.metric=='lmnn'):    
            self.preproc=metric_learn.lmnn.LMNN(k=self.k)
            self.preproc.fit(X,dataset.y)
            X=self.preproc.transform(X)
        self.clf.fit(X,dataset.y)

    def __call__(self,sample,single=True):
        if(self.preproc!=None):
            sample=self.preproc.transform(sample)
        pred=self.clf.predict(sample)
        if(single):
            return pred[0]
        else:
            return pred

class Condensate(object):
    def __init__(self,k):
        self.k=k 

    def __call__(self,dataset):
        data1=remove_outliners(dataset,self.k)  
        return remove_redundant(data1,self.k)

def remove_outliners(dataset,k=1):
    knn=KNN(k)
    knn.train(dataset)
    no_outliners=[]
    for i,x_i in enumerate(dataset.X):
        pred_i=knn(x_i)
        if(pred_i==dataset.y[i]):
            no_outliners.append(i)
    return dataset.select(no_outliners)

def remove_redundant(dataset,k=1):
    def train_knn(dataset):
        knn=KNN(k)
        knn.train(dataset)
        return knn
    x_0,y_0=dataset[0]
    new_dataset=gen.Dataset([x_0],[y_0])
    knn_model=train_knn(new_dataset)
    for i in range(len(dataset)):
        x_i,y_i=dataset[i]
        pred_y=knn_model(x_i)
        if(pred_y!=y_i):
            new_dataset.add(x_i,y_i)
            knn_model=train_knn(new_dataset)
    return new_dataset