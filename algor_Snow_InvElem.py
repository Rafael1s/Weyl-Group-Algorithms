import numpy as np
from reflections_D4 import root_system, refl, Cmatr, Nlevels
from element import Element, weightToStr

len_weight = len(Cmatr) 

def buildLevel_0(oneLevel):
      
   start_weight = np.ones(len_weight, dtype=int).tolist()
   unit_matr = np.eye(len_weight, dtype=int).tolist()         
   elm = Element(weight=start_weight, name=' ', name_inv = ' ', \
                 matr=unit_matr, matr_inv=unit_matr, n_in_lvl = 0)

   elm.n_inv_in_lvl = 0
   oneLevel.append(elm)

def newPossibleWeight(numbRefl,  weight, mi):
    new_possible_weight = []
    for jW in range(len_weight):
        ''' The main formula of Snow's alg '''
        new_coord =  weight[jW] - mi*Cmatr[jW][numbRefl]
        new_possible_weight.append(new_coord) 
    return new_possible_weight   

def newElem(iRefl, new_weight, name, name_inv, matr, matr_inv, new_n_in_lvl):

    ''' new_n_in_lvl = the following place in the oneLevel, i.e. = len(one_level) '''
    iW = iRefl - 1
    if (name == ' '):
       new_name_inv = new_name        = str('s') + str(iRefl)
       new_matr_inv = new_matr        = refl[iW]
    else:   
       new_name     = str('s') + str(iRefl) + str('.') + name
       new_name_inv = name_inv + str('.s') + str(iRefl) 
       new_matr     = np.matmul(refl[iW], matr)
       new_matr_inv = np.matmul(matr_inv, refl[iW])
    
    new_elem = Element(new_weight, new_name, new_name_inv, new_matr, new_matr_inv, new_n_in_lvl)    
    
    return new_elem


def findAllLevels_to_LvlK(prefix, list_of_all_levels, lvlK):

  len_by_all_levels = 0

  for ik in range(lvlK):
     ''' Get Lvl(k) and create Lvl(k+1) '''
     oneLevel = list_of_all_levels[ik] 
     new_level = [] 
     dictElemsOfLevel =  {} 
     len_by_all_levels =  len_by_all_levels + len(oneLevel)
          
     for iElem in range(len(oneLevel)):
          elem = oneLevel[iElem]
          ''' get elements of the previous level = ik to construct the new_level = (ik+1) '''           
          weight = elem.weight
             
          ''' iRefl is  the numb of reflection '''
          for iW in range(len_weight):
            iRefl = iW + 1            
            if  weight[iW] > 0:
                mi = weight[iW]
                new_candidate_weight = newPossibleWeight(iW, weight, mi)
                '''sShould be unique Weight '''
                uniqueFlag = True
                if (iW == len_weight - 1):
                    uniqueFlag =True
                else:    
                    for iUniq in range(iW+1, len_weight):
                       if new_candidate_weight[iUniq] < 0:
                           uniqueFlag = False
                           break
                       
                if uniqueFlag is True:                   
                    ''' This the element of order 2 '''
                    new_n_in_lvl = len(new_level)
                    new_elm = newElem(iRefl, new_candidate_weight, 
                                      elem.name, elem.name_inv, 
                                      elem.matr, elem.matr_inv, new_n_in_lvl)

                    if new_elm.ifSelfInverseMatr():
                        new_elm.n_inv_in_lvl = new_elm.n_in_lvl
                        ''' no need to save this elem in dictionary, it's ok with its inverse'''
                        new_level.append(new_elm)
                    else:    
                        key, key_inv, val = new_elm.keyValAndKeyInv()
                        
                        if key in dictElemsOfLevel.keys():
                           ''' the partner (inverse) already wait for this key'''
                           ''' relate 'new_elem_inv' and 'new_elm'  '''
                           val = dictElemsOfLevel[key]
                           n_in_lvl = int(val)
                           new_elem_inv = new_level[n_in_lvl]
                           new_elem_inv.n_inv_in_lvl = new_elm.n_in_lvl
                           new_elm.n_inv_in_lvl = new_elem_inv.n_in_lvl
                           new_level.append(new_elm)
                        else: 
                           new_elm.n_in_lvl = len(new_level) 
                           ''' info to the parther(inverse) about lovcation of new element'''
                           val = str(new_elm.n_in_lvl)
                           dictElemsOfLevel[key_inv] = val 
                           new_level.append(new_elm)
                                              
     list_of_all_levels.append(new_level)      
          
     writeOneLevel(ik+1, new_level, prefix)     
     
  print('len_by_all_levels: ', len_by_all_levels)       

  how_many_elems = 0
  
  for iLvl in range(len(list_of_all_levels)):
       n_elems = len(list_of_all_levels[iLvl])
       how_many_elems = how_many_elems + n_elems   
                        
  print(' Total.number.of.elements.in: ' + root_system + ': ',  how_many_elems)  
    
''' single level recoding procedure: 
    ik - level number, oneLevl - a level from list_of_all_levels,
    prefix - string root system: "D4", "B5", etc.'''  
def writeOneLevel(ik, oneLevel, prefix):
    
    n_elems = len(oneLevel)
    
    if n_elems == 0:
        return
       
    file_name = prefix + '_WeightMatrByLevel_' + str(ik) +\
            '_elems=' + str(n_elems) + '.txt'
    path_to_file = prefix + '_DataFiles\\' + file_name
    print('write file: ', path_to_file)
    with  open(path_to_file, 'w') as f:
         
        '''in 'weight' the last comma already there '''
        for iElem in range(len(oneLevel)):
            elem = oneLevel[iElem]  
            wStr = weightToStr(elem.weight)
            lineElem = 'n='+ str(elem.n_in_lvl) +\
                        ', name=' + elem.name +\
                        ', w=' + wStr +\
                        ', n_inv=' + str(elem.n_inv_in_lvl)
            f.write(lineElem)
            for r in elem.matr:
                line = list(r)  
                f.write('\n')
                f.write(str(line))    
            f.write('\n')
        f.close()     


       
if __name__ == "__main__":
   
    list_of_all_levels = [] 
    len_weight = len(Cmatr) 
    oneLevel = []

    ''' Step 0'''
    buildLevel_0(oneLevel)
    writeOneLevel(0, oneLevel, root_system)
    
    list_of_all_levels.append(oneLevel)
    
    ''' Here, function writeOneLevel is called for each level '''
    findAllLevels_to_LvlK(root_system,  list_of_all_levels, lvlK=Nlevels) 