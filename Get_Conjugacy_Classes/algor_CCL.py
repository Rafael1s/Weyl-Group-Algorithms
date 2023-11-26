from reflections_D4 import root_system, Cmatr, Nlevels

from find_conj_classes import findConjugacyClasses_With_Dict
from readLevels import readAllLevels_With_Dict

if __name__ == "__main__":
   
    list_of_all_levels = [] 
    dictAllElems =  {} 
    readAllLevels_With_Dict(list_of_all_levels, dictAllElems, \
                    matr_size=len(Cmatr), Nlevels=Nlevels, prefix=root_system)
        
    all_CCLs = []
    findConjugacyClasses_With_Dict(list_of_all_levels, dictAllElems, \
                                   all_CCLs, Nlevels, prefix=root_system) 
    
    all_elems = 0
    for j in range(len(all_CCLs)):
        elems_in_ccl = len(all_CCLs[j])
        all_elems = all_elems + elems_in_ccl
        
    print('numb.elem.in.all.CCLs: ', all_elems)
        
    