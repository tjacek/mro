import gen
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import knn,visualization

class Experiment(object):
    def __init__(self,gen,model):
        self.gen=gen
        self.model=model

    def pred(self,dataset):
    	return [ self.model(x_i) for x_i in dataset.X]

    def split(self,dataset):
        train=dataset.select(gen.Modulo(0))
        test=dataset.select(gen.Modulo(1))
        return train,test

class SimpleExperiment(Experiment):
    def __init__(self,gen,model):
        super(SimpleExperiment, self).__init__(gen,model)
                
    def __call__(self,n=500,show=False):
        dataset=self.gen(n)
        train,test=self.split(dataset)
        self.model.train(train)
        y_pred=self.pred(test)
        y_true=test.y
        print(classification_report(y_true, y_pred,digits=4))
        if(show):
            visualization.decision_boundary(dataset,self.model)

class SelectExperiment(Experiment):
    def __init__(self,gen,model,select_fun):
        super(SelectExperiment, self).__init__(gen,model)
        self.select_fun=select_fun

    def __call__(self,n=500,show=False):
        dataset=self.gen(n)
        train,test=self.split(dataset)
        train.show()
        s_train=self.select_fun(train)
        s_train.show()
        self.model.train(s_train)
        y_pred=self.pred(test)
        y_true=test.y
        print(classification_report(y_true, y_pred,digits=4))
        if(show):
            test+=s_train
            visualization.decision_boundary(test,self.model)