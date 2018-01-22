import numpy as np 

class Cls(object):
    def __init__(self,model):
        self.model=model

    def __call__(self,dataset):
        y_pred=self.clf.predict(dataset.X)