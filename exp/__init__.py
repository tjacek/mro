import gen
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import knn,visualization

class TrainExperiment(object):
    def __init__(self,gen,model):
        self.gen=gen
        self.model=model

    def pred(self,dataset):
    	return [ self.model(x_i) for x_i in dataset.X]

    def split(self,dataset):
        train=dataset.select(gen.Modulo(0))
        test=dataset.select(gen.Modulo(1))
        return train,test

