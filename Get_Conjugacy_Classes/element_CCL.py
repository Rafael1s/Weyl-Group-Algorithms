def consructKey(matr):
    key = ''.join(str(i) for row in matr for i in row)  
    return key

class Element_CCL(object):
    def __init__(self, name, name_inv, matr, level, n_in_lvl, n_inv_in_lvl):
        ## self.weight  = weight
        self.name    = name
        self.name_inv    = name_inv
        self.matr    = matr
        self.matr_inv =  -1
        self.level = level
        ''' if n_in_lvl == n_inv_in_lvl ==> order = 2'''
        self.n_in_lvl = n_in_lvl
        ''' at the begining, we don't know number of inv elem in level '''
        self.n_inv_in_lvl = n_inv_in_lvl
        self.ccl = -1
    
    def keyAndComplexVal(self, level):
        key = consructKey(self.matr)         
        val = str(level) + ',' + str(self.n_in_lvl)
        return key, val 
    