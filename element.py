import numpy as np

def isIdentity(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
           if i == j and M[i][j] != 1:
               return False
           elif i!=j and M[i][j]!=0:
               return False
    return True

def weightToStr(weight):
    w = ''
    for i in range(len(weight)):
        if i < len(weight)-1:
            w = w + str(weight[i]) + ','
        else:
            w = w + str(weight[i])
    return w

class Element(object):
    def __init__(self, weight, name, name_inv, matr, matr_inv, n_in_lvl):
        self.weight  = weight
        self.name    = name
        self.name_inv    = name_inv
        self.matr    = matr
        self.matr_inv =  matr_inv
        ''' if n_in_lvl == n_inv_in_lvl ==> order = 2'''
        self.n_in_lvl = n_in_lvl
        ''' at the begining, we don't know number of inv elem in level '''
        self.n_inv_in_lvl = -1

    def keyValAndKeyInv(self):
        key     = ''.join(str(i) for row in self.matr for i in row)  
        key_inv = ''.join(str(i) for row in self.matr_inv for i in row)  
        val = str(self.n_in_lvl)
        return key, key_inv, val
    
    def ifSelfInverseMatr(self):
        prod = np.matmul(self.matr, self.matr)
        return isIdentity(prod)
