
from BilinearForm import getBilForm
from PositiveRoots import PositiveRoots as pr

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
        #print(*self.rlist, sep='\n')
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
if __name__ == "__main__":   
     rlen = RootLength('C',7)                    
     rlen.printRoots()
     #rlen.printListOfRoots_by_height()