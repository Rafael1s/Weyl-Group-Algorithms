
maxRoot_E6 = [1,2,2,3,2,1]

maxRoot_E7 = [2,2,3,4,3,2,1]

maxRoot_E8 = [2,3,4,6,5,4,3,2] 

maxRoot_F4 = [2,3,4,2]  

maxRoot_G2 = [2,3]

def getMaxRootAn(n):
    max_root = [1]*n
    return max_root 

def getMaxRootBn(n):
    max_root = [2]*n
    max_root[0] = 1
    return max_root 

def getMaxRootCn(n):
    max_root = [2]*n
    max_root[n-1] = 1
    return max_root 

def getMaxRootDn(n):
    max_root = [2]*n
    max_root[0] = 1
    max_root[n-2] = 1
    max_root[n-1] = 1
    return max_root 

def getMaxRootEn(n):
    if n == 6:
       return maxRoot_E6
    elif n == 7:
       return maxRoot_E7
    elif n == 8:
       return maxRoot_E8
   
def getMaxRootG2():        
    return maxRoot_G2
   
def getMaxRootF4():
    return maxRoot_F4

def getMaxRoot(diagram, n):
    if diagram == 'E': 
        return getMaxRootEn(n)
    elif diagram == 'F':
        return getMaxRootF4()  
    elif diagram == 'G':
        return getMaxRootG2()
    elif diagram == 'A':
        return getMaxRootAn(n)
    elif diagram == 'B':
        return getMaxRootBn(n)
    elif diagram == 'C':
        return getMaxRootCn(n)
    elif diagram == 'D':
        return getMaxRootDn(n)

if __name__ == "__main__": 
    mr = getMaxRootG2()
    print('max_root for G2: ', mr, '\n')
    mr = getMaxRootF4()
    print('max_root for F4: ', mr, '\n')
    mr = getMaxRootAn(5)
    print('max_root for A5: ', mr, '\n')
    mr = getMaxRootBn(6)
    print('max_root for B6: ', mr, '\n')
    mr = getMaxRootCn(5)
    print('max_root for C5: ', mr, '\n')
    mr = getMaxRootDn(8)
    print('max_root for D8: ', mr, '\n')
    