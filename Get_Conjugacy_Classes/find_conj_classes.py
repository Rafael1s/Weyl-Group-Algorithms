import numpy as np
from element_CCL import consructKey

''' Let w0 denote the unique Weyl group element of maximum length. 
Length l(w0) is equal to the number of positive roots 
in the Weyl group W. Then, Nlevels =  number of positive roots + 1'''

def isIdentity(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
           if i == j and M[i][j] != 1:
               return False
           elif i!=j and M[i][j]!=0:
               return False
    return True

def checkPower(M):
    
    A = M
    
    for i in range(0,100):
        ''' i = 0 = ==> power = 2 
            i = 1 = ==> power = 3 '''        
        A = np.matmul(A, M)
        if isIdentity(A):
            return (i+2)
    return -1    

def matrOfInverse(oneLevel, elem):
     loc_inv = int(elem.n_inv_in_lvl) ## - 1       
     return oneLevel[loc_inv].matr       
    
def findCCLForEelement_With_Dict(list_of_all_levels, dictAllElems, elem, \
                                 oneConjClass, conj_cl_number, Nlevels, prefix):

    setOneCCL = set()
    oneConjClass.append(elem)
    key = consructKey(elem.matr)
    setOneCCL.add(key)
            
    if isIdentity(elem.matr) == True:
        elem.ccl = conj_cl_number
        elem.name = 'e'
        elem.n_in_lvl = 1
    else:        
        elem.ccl = conj_cl_number
    
        for ik in range(1, Nlevels):
            oneLevel = list_of_all_levels[ik] 
       
            for iElem in range(len(oneLevel)):
               a_elem = oneLevel[iElem]   
            
               matr_inv_a_elem = matrOfInverse(oneLevel, a_elem)                            
               matr_prom = np.matmul(a_elem.matr, elem.matr)
               conj_matr = np.matmul(matr_prom, matr_inv_a_elem)
            
               key = consructKey(conj_matr)
               
               alreadyInSet = key in setOneCCL

               if alreadyInSet == False:
                   ''' val = str(level) + ',' + str(self.n_in_lvl) '''
                   val = dictAllElems[key]
               
                   x = val.split(',')
                   level =  int(x[0])
                   n_in_lvl =  int(x[1])  ### - 1 ???
               
                   oneLevel_of_conjMatr = list_of_all_levels[level]
                   conj_elem = oneLevel_of_conjMatr[n_in_lvl]               
                   conj_elem.ccl = conj_cl_number
               
                   oneConjClass.append(conj_elem) 
                   setOneCCL.add(key)
                       
            
''' from class 'frm' to class 'to' '''
def findConjugacyClasses_With_Dict(list_of_all_levels, dictAllElems, all_ConjClasses, Nlevels, prefix):

    conj_cl_numb = 0
                    
    for ik in range(0, Nlevels):
   
       oneLevel = list_of_all_levels[ik] 
              
       for iElem in range(len(oneLevel)): 
           
            elem = oneLevel[iElem]    
                        
            if int(elem.ccl) == -1:         
                
                print('conj_cl: ', conj_cl_numb , ', representative elem (lvl, n) ', \
                      ik, elem.n_in_lvl)
                
                oneConjClass = []

                findCCLForEelement_With_Dict(list_of_all_levels, dictAllElems, elem, \
                                 oneConjClass, conj_cl_numb, Nlevels, prefix)
                
                all_ConjClasses.append(oneConjClass)
                
                writeOneConjClass(conj_cl_numb, oneConjClass, prefix)

                conj_cl_numb = conj_cl_numb + 1
                
    print('number of Conj Classes: ', conj_cl_numb)
        
def writeOneConjClass(conj_cl_numb, oneConjClass, prefix):
    
       n_elemsConjCl = len(oneConjClass)
       print('writeOneConjClass, len: ', n_elemsConjCl)
                     
       pattern_order = -1
       if isIdentity(oneConjClass[0].matr):
           pattern_order = 1
       elif oneConjClass[0].n_in_lvl ==  oneConjClass[0].n_inv_in_lvl :
           pattern_order = 2 
       else:              
           pattern_order = checkPower(oneConjClass[0].matr)
       
       file_name = prefix + '_CCL_' + \
             str(conj_cl_numb) + '_ord=' + str(pattern_order)  \
                     + '_elms=' + str(n_elemsConjCl) + '.txt'
                     
       print('file_name: ', file_name)              
                     
       path_to_file = prefix + '_CCL\\' + file_name
       
       with  open(path_to_file, 'w') as f:
         
           n_in_ConjCl = 0
           '''in weihgt last comma already in '''
           for iElem in range(len(oneConjClass)):
               elem = oneConjClass[iElem]  
               n_in_ConjCl = n_in_ConjCl + 1
               lineElemInConjCl = 'n='+ str(n_in_ConjCl) +\
                        ', level=' + str(elem.level) +\
                        ', name='  + elem.name +\
                        ', n_in_lvl=' + str(elem.n_in_lvl)+\
                        ', name_inv=' + elem.name_inv
               f.write(lineElemInConjCl)
               for r in elem.matr:
                   line = list(r)  
                   f.write('\n')
                   f.write(str(line))    
               f.write('\n')
           f.close()           
               

