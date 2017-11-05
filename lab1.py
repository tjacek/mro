import gen,gen.dists
import gen.conic,gen.preds
import exp
import knn

def make_gen1():
    dist=gen.dists.NormalDist()	
    preds=[get_non_convex(),gen.conic.Ellipse(0.9,2.5)]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

def make_gen2():
    dist=gen.dists.UniformDist([-5.0,-5.0],10.0)
    ref_triang=gen.preds.ReflectedTriangles([-2.0,2.0],[0.0,0.0],[2.0,2.0])
    preds=[ref_triang,gen.conic.Hiperbola(1.5,1.8)]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

def make_gen3():
    dist=gen.dists.UniformDist([-5.0,-5.0],10.0)
    over_triang=gen.preds.OverlapingTriangles([-3.0,2.0],[-2.0,0.0],[-1.0,2.0],1.0)
    preds=[over_triang,gen.preds.ElipticCurve(0.9,2.5)]
    my_gen=gen.GenerateDataset(dist,preds)
    return my_gen

def get_non_convex():
    return gen.preds.SimpleNonConvex([1.0,1.0],[-1.0,1.0],[0.0,0.0],[0.0,-1.0])

my_gen=make_gen3()
dataset=my_gen(1500)
dataset.show()
#exp1=exp.SelectExperiment(my_gen,knn.KNN(k=1),knn.Condensate(k=1))
#exp1(500,True)

#metr=['mahalo','lmnn']
#dataset=my_gen(1000)
#dataset.show()
#s_dataset=knn.remove_outliners(dataset)
#s_dataset.show()
#s_dataset=knn.remove_redundant(dataset)
#s_dataset.show()
#exp1=exp.Experiment(my_gen,knn.KNN(k=1,metric='lmnn'))#'mahalo'))
#exp1(250,True)