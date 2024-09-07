## Developed by Rafael Stekolshchik. July, 2024

from BilinearForm import getBilForm
from PositiveRoots import PositiveRoots as pr

import numpy as np

class InnerProduct(object):
    def __init__(self, diagram, n):
       self.n = n 
       self.diagram = diagram 
       self.bil_matr = getBilForm(diagram, n) 
       self.pr = pr(diagram, n)       
       self.rlist = self.pr.getRootlist()       
       self.dim = len(self.rlist)
       self.matrProd = np.full((self.dim,self.dim), -99.9) 
       self.indexOfRoot =self.pr.indexOfRoot
       self.getInnerProdForAllPairs()

    def innerProduct(self, i, j):    
       s0 = 0
       root_a = self.rlist[i]
       root_b = self.rlist[j]
       for ka in range(len(root_a)):
          for kb in range(len(root_b)):
             s0 = s0 + self.bil_matr[ka][kb]*root_a[ka]*root_b[kb]              
       return s0    

    def scalarSquare(self, root):    
       s0 = 0
       for i in range(len(root)):
          for j in range(len(root)):
              s0 = s0 + self.bil_matr[i][j]*root[i]*root[j]              
       return s0    
   
    def printRoots(self):
        for i in range(len(self.rlist)): 
            sc = self.scalarSquare(self.rlist[i])
            print(i, ') ', self.rlist[i], ' ## sq.len: ', sc)
                    
    def printListOfRoots_by_height(self):
      count = 0  
      j = 0
      current_ht = 0
      for root in self.rlist:
            ht = sum(root)
            j += 1
            if ht > current_ht:
                print(count,') ', root, '  ht: ', ht)  
                current_ht = ht
            else:   
                print(count,') ', root)  
            count += 1      
            
    def getInnerProdForAllPairs(self):
        for i in range(len(self.rlist)):
           for j in range(i+1, len(self.rlist)):    
               prod = self.innerProduct(i,j)
               self.matrProd[i][j], self.matrProd[j][i] = prod, prod
        for i in range(len(self.rlist)):
            self.matrProd[i][i] = self.innerProduct(i,j)           

    def othhogRoots_with_sumIsRoot(self):
       i_p = 0
       for i in range(len(self.rlist)):
          for j in range(i+1, len(self.rlist)):
              iprod = self.innerProduct(i, j)
              if iprod == 0:
                  vec_ij = [x + y for x,y in zip(self.rlist[i], self.rlist[j])]
                  isum = self.indexOfRoot(vec_ij) 
                  if isum != -1:
                      i_p += 1
                      print(i_p, ')  i, j, isum: ', i, j, isum, 
                            ' orthog pair, but ri+rj is root') 
                      print('      ', self.rlist[i], self.rlist[j], 
                                self.rlist[isum])
    
    def replace(self, i):
       if i >= 0:
          return ' ' + str(i)
       else:
          return str(i)
      
    def printMatrInnerProducts(self):
        print('\n=======  Matr Inner Produvst =======')
        for i in range(len(self.matrProd)):
            line = []
            for j in range(len(self.matrProd[i])):
                Pij = self.matrProd[i][j] 
                line.append(Pij)    
            an_line =  ''.join(self.replace(j) for j in line)  
            print(i, ',) ', an_line)                      
        
    
if __name__ == "__main__":   
     rlen = InnerProduct('F',4)                    
     #rlen.printRoots()
     #rlen.printListOfRoots_by_height()
     
     #i,j = 2, 23
     #prd = rlen.innerProduct(i,j)
     #print('i, j, inner_prod: ', i, j, prd)
     
     
     rlen.printMatrInnerProducts()
     
     
     