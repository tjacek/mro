import numpy as np 
from sklearn import svm

class Cls(object):
    def __init__(self,C):
        self.model= svm.SVC(C=1.0,decision_function_shape='ovo')

    def __call__(self,dataset):
        y_pred=self.clf.predict(dataset.X)