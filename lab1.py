import gen
import gen.ellipse,gen.preds
import exp
import knn

def make_gen():
    dist=gen.NormalDist()	
    preds=[get_non_convex(),gen.ellipse.Ellipse(0.9,2.5)]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

def get_non_convex():
    return gen.preds.SimpleNonConvex([1.0,1.0],[-1.0,1.0],[0.0,0.0],[0.0,-1.0])

metr=['mahalo','lmnn']
my_gen=make_gen()
exp1=exp.Experiment(my_gen,knn.KNN(k=1,metric='lmnn'))#'mahalo'))
exp1(250,True)