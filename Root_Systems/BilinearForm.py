## Developed by Rafael Stekolshchik. July, 2024

import numpy as np
 
matrBilForm_E6 = \
[[1,    0, -1/2,    0,    0,   0],
 [0,    1,  0,   -1/2,    0,   0],
 [-1/2 ,0,  1,   -1/2,    0,   0],
 [0,  -1/2,-1/2,    1,  -1/2,  0],
 [0,    0,  0,   -1/2,    1, -1/2],
 [0,    0,  0,      0,   -1/2, 1]]

matrBilForm_E7 = \
[[ 1,   0,  - 1/2,    0, 0,   0,  0],
 [ 0,   1,    0,  - 1/2, 0,   0,  0],
 [-1/2, 0,    1,   -1/2, 0,   0,  0],
 [ 0,  -1/2, -1/2,    1,-1/2, 0,  0],
 [ 0,   0,    0,  -1/2,  1,-1/2,  0],
 [ 0,   0,    0,      0,-1/2, 1,-1/2],
 [ 0,   0,    0,      0, 0, -1/2, 1]]

matrBilForm_E8 = \
[[ 1,   0, -1/2,   0,   0,   0,   0,   0],
 [ 0,   1,    0, -1/2,  0,   0,   0,   0],
 [-1/2, 0,    1, -1/2,  0,   0,   0,   0],
 [ 0,-1/2, -1/2,   1, -1/2,  0,   0,   0],
 [ 0,   0,    0,  -1/2, 1, -1/2,  0,   0],
 [ 0,   0,    0,   0, -1/2,  1, -1/2 , 0],
 [ 0,   0,    0,   0,   0, -1/2,  1,-1/2],
 [ 0,   0,    0,   0,   0,   0,  -1/2, 1]] 

matrBilForm_F4 = \
[[ 2,  -1,  0,    0],
 [-1,   2, -1,    0],
 [ 0,  -1,  1, -1/2],
 [ 0,   0, -1/2,  1]]

matrBilForm_G2 = \
[[3, -3/2],
 [-3/2, 1]]

def getEn(n):
    if n == 6:
       return matrBilForm_E6
    elif n == 7:
       return matrBilForm_E7
    elif n == 8:
       return matrBilForm_E8
   
def getF4():
    return matrBilForm_F4
      
def getG2():        
    return matrBilForm_G2
        
def getAn(n):
    matrBilForm = []
    for i in range(0,n):
       if i == 0:
         lin = [0]*n
         lin[0] = 1
         lin[1] = -1/2
         matrBilForm.append(lin)
       elif i > 0 and i < n-1:
         lin = [0]*n
         lin[i-1] = -1/2
         lin[i] = 1
         lin[i+1] = -1/2
         matrBilForm.append(lin)
       elif i == n-1:
         lin = [0]*n
         lin[n-2] = -1/2           
         lin[n-1] = 1           
         matrBilForm.append(lin)
    return matrBilForm      

def getBn(n):    
    matrA = getAn(n)
    matrA_np = np.array(matrA)
    M = 2*matrA_np    
    matrBilForm = M.tolist()    
    matrBilForm[n-1][n-1] = 1 
    return matrBilForm

def getCn(n):    
    matrBilForm = getAn(n)
    matrBilForm[n-2][n-1] = -1
    matrBilForm[n-1][n-2] = -1
    matrBilForm[n-1][n-1] =  2
    return matrBilForm

def getDn(n):    
    matrBilForm = getAn(n)
    matrBilForm[n-3][n-1] = -1/2
    matrBilForm[n-2][n-1] = 0
    matrBilForm[n-1][n-3] = -1/2
    matrBilForm[n-1][n-2] = 0
    return matrBilForm

def getBilForm(diagram, n):
    if diagram == 'E': 
        return getEn(n)
    elif diagram == 'F':
        return getF4()  
    elif diagram == 'G':
        return getG2()
    elif diagram == 'A':
        return getAn(n)
    elif diagram == 'B':
        return getBn(n)
    elif diagram == 'C':
        return getCn(n)
    elif diagram == 'D':
        return getDn(n)

if __name__ == "__main__":    
    matr = getBilForm('G',2)
    print(' ', 'G =', *matr, sep = '\n')
    matr = getBilForm('F', 4)
    print(' ', 'F =', *matr, sep = '\n')
    matr = getBilForm('B', 5)
    print(' ', 'B5 =', *matr, sep = '\n')
    matr = getBilForm('C', 5)
    print(' ', 'C5 =', *matr, sep = '\n')
    matr = getBilForm('E', 6)
    print(' ', 'E6 =', *matr, sep = '\n')
    matr = getBilForm('E', 7)
    print(' ', 'E7 =', *matr, sep = '\n')
    matr = getBilForm('E', 8)
    print(' ', 'E8 =', *matr, sep = '\n')
    matr = getBilForm('A', 9)
    print(' ', 'A9 =', *matr, sep = '\n')
    matr = getBilForm('D', 10)
    print(' ', 'D10 =', *matr, sep = '\n')
    