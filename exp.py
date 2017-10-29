import gen
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import knn

class Experiment(object):
    def __init__(self,gen,model):
        self.gen=gen
        self.model=model

    def __call__(self,n=500,show=False):
        dataset=self.gen(n)
        train,test=self.split(dataset)
        self.model.train(train)
        y_pred=self.pred(test)
        y_true=test.y
        print(classification_report(y_true, y_pred,digits=4))
        if(show):
#           dataset.show()
            knn.decision_boundary(dataset,self.model.clf)

    def pred(self,dataset):
    	return [ self.model(x_i) for x_i in dataset.X]

    def split(self,dataset):
        train=dataset.select(gen.Modulo(0))
        test=dataset.select(gen.Modulo(1))
        return train,test