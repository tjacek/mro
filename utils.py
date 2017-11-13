from sets import Set
import copy

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
