from sets import Set
import copy
import cv2

def read_img(path):
    raw_img=cv2.imread(str(dir_path),cv2.IMREAD_GRAYSCALE) 
    return raw_img 

def all_seq(length,base_symbols,seqs=[]):
    if(length==0):
        return seqs	
    def seq_helper(base_j,old_seq_i):
        new_seq_ij=copy.copy(old_seq_i)
    	new_seq_ij.append(base_j)
        return new_seq_ij
    new_seqs=[ seq_helper(base_j,old_seq_i)
                for base_j in base_symbols
                    for old_seq_i in seqs]
    if(not new_seqs):
        new_seqs=[ [base_i] for base_i in base_symbols]   
    return all_seq(length-1,base_symbols,new_seqs)

def scalar_pred(scalar,less=True):
    if(less):
        return lambda x: x<scalar
    else:
        return lambda x: x>scalar

class MultiScalarPred(object):
    def __init__(self,lower,upper):
        self.lower=lower
        self.upper=upper
    
    def __call__(self,point):
        bool_values=[ self.lower[i]<point_i and point_i<self.upper[i]  
                        for i,point_i in enumerate(point)]
        return any(bool_values)
    