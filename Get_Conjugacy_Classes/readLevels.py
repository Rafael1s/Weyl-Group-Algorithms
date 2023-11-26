import os
import collections

from element_CCL import Element_CCL

def getLevelFiles(prefix, pattern):
  path_dir = prefix + '_Levels' 
       
  dict_files = {}
  for f in os.listdir(path_dir):
      if pattern in f:
          x =  f.split('_')
          ''' X[2] is the number of Level in str format '''
          dict_files[int(x[2])] = f
            
  files = collections.OrderedDict( 
          sorted(dict_files.items(), key = lambda x: int(x[0])))
  
  return files

def deleteBrackets(line):
    line_to_return = ' '
    k = line.find('[', 0)

    if k == 0:
       line = line[1:]
   
    k = line.find(']', 0)

    if k > 0:
      line_to_return = line.rstrip(line[-1])
       
    return line_to_return   

def getListOfInt(line):
     list_int = []
     x = line.split(",")

     for i in range(len(x)):
        j =  int(x[i])
        list_int.append(j)
     return list_int    
        
def parseLineOfElem_Level(line_elem, level, matr):
    
   ''' x[0] = n, 
       x[1] = 0, name 
       x[2] = s3.s2.s1, w
       x[3] = 1,1,-3,3, n_inv, 
       x[4] = 9
   '''
   x = line_elem.split("=")

   ''' number in level'''
   n = x[1].split(',')
   
   ''' name like s2.s4.s3.s2.s1 '''
   name = x[2].split(',')

   ''' weight = x[3].split(' ') '''
   
   ''' number of inverse matrix in level  '''
   n_inv = x[4]
             
   elem = Element_CCL(name=name[0], name_inv = ' ',  level = level,
                      matr=matr,  n_in_lvl = int(n[0]), n_inv_in_lvl = int(n_inv) )
         
   return elem

    
def readOneLevel_With_Dict(oneLevel, dictAllElems, level_files, lvl_numb, matr_size, prefix):
    
    path_to_file = prefix + '_Levels\\' + level_files[lvl_numb]
    
    print('Read Level ', lvl_numb)
        
    with  open(path_to_file, 'r') as f:
        ''' No newlines '\n' After read().splitlines() '''
        all_lines = f.read().splitlines()
        
        iLine = 0

        while iLine < len(all_lines):
            lineElem = all_lines[iLine]            
            matr = []
            
            for iMatr in range(iLine+1, iLine + 1 + matr_size):

                line = all_lines[iMatr]
                line = deleteBrackets(line)
                list_int = getListOfInt(line)
                matr.append(list_int)

            elem = parseLineOfElem_Level(lineElem, lvl_numb, matr)  
            
            iLine = iLine + matr_size + 1
            
            key, val = elem.keyAndComplexVal(lvl_numb)

            dictAllElems[key] = val

            oneLevel.append(elem)
            
        for iElem in range(len(oneLevel)):
             elem = oneLevel[iElem]
             
             if elem.matr_inv == -1:                
                n_inv_in_lvl = elem.n_inv_in_lvl
                elem_inv = oneLevel[n_inv_in_lvl]
                elem.name_inv = elem_inv.name
                elem_inv.name_inv = elem.name
                elem.matr_inv = elem_inv.matr
                elem_inv.matr_inv = elem.matr 
                elem.n_inv_in_lvl = elem_inv.n_in_lvl
                elem_inv.n_inv_in_lvl = elem.n_in_lvl
                

def readAllLevels_With_Dict(list_of_all_levels, dictAllElems, \
                            matr_size, Nlevels, prefix):
        
    level_files = getLevelFiles(prefix, 'Level_')
    
    for ik in range(Nlevels):        
        
        oneLevel = []
        readOneLevel_With_Dict(oneLevel, dictAllElems, level_files, lvl_numb=ik, 
                     matr_size=matr_size, prefix=prefix)     
        
        list_of_all_levels.append(oneLevel)

            
if __name__ == "__main__":
 
   from reflections_D4 import root_system, Cmatr, Nlevels       
   list_of_all_levels = [] 
   dictAllElems =  {} 
   readAllLevels_With_Dict(list_of_all_levels, dictAllElems, \
                    matr_size=len(Cmatr), Nlevels=Nlevels, prefix=root_system)
        
   print('numb.elem.in.dictAllElems: ', len(dictAllElems.keys()))       
   