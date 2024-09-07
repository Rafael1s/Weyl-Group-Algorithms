## Developed by Rafael Stekolshchik. July, 2024

from BilinearForm import getBilForm
from PositiveRoots import PositiveRoots as pr

def innerProd(root_a, root_b, bil_matr):    
    s0 = 0
    for i in range(len(root_a)):
       for j in range(len(root_b)):
           s0 = s0 + bil_matr[i][j]*root_a[i]*root_b[j]              
    return s0    

class RootLength(object):
    def __init__(self, diagram, n):
       self.n = n 
       self.diagram = diagram 
       self.bil_matr = getBilForm(diagram, n) 
       self.pr = pr(diagram, n)
       self.rlist = self.pr.getRootlist()       

    def scalarSquare(self, root):    
       s0 = 0
       for i in range(len(root)):
          for j in range(len(root)):
              s0 = s0 + self.bil_matr[i][j]*root[i]*root[j]              
       return s0    
   
    def printRoots(self):
        for i in range(len(self.rlist)): 
            sc = self.scalarSquare(self.rlist[i])
            print(i, ')  ', self.rlist[i], '   ', int(sc) )
                        
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
if __name__ == "__main__":   
     rlen = RootLength('F',4)                    
     rlen.printRoots()
     rlen.printListOfRoots_by_height()
     
     