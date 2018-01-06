import gen,gen.conic,gen.dists

def make_sphere_gen(dim):
    start=[ -1.0 for i in range(dim)]
    dist=gen.dists.UniformDist(start ,width=1.0)	
    preds=[gen.conic.Radius(1.0)]
    sphere_gen=gen.GenerateDataset(dist,preds)
    def proportion(n):
    	sphere_data=sphere_gen(n)
        y=sphere_data.y
    	return sum(y)/float(len(y))
    return proportion

cube=make_sphere_gen(5)
print(cube(1000))