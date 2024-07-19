
import exc_root_lists as erl
from CoxeterNumber import getCoxeterNumber    

class PositiveRoots(object):
    def __init__(self, diagram, n):
       self.n = n 
       self.coxNumber = getCoxeterNumber(diagram, n)  
       self.diagram = diagram 
       self.rlist = []
       self.collectRoots()
                
    def indexOfRoot(self, root):
        try:
          ind = self.rlist.index(root)
        except ValueError:
          ind = -1
        return ind
              
    def rootsAn(self, n):
         list_An = []
         for i in range(0, n):             
            for j in range(i, n):
                root = [0]*i + [1]*(j-i+1) + [0]*(n-j-1)   
                list_An.append(root)
         return list_An 
     
    def rootsBn(self, n):
         list_Bn = self.rootsAn(n)
         for i in range(0, n):
            for j in range(i+1,n): 
              eps_i = [0]*i + [1]*(n-i)
              eps_j = [0]*j + [1]*(n-j) 
              root = [x + y for x,y in zip(eps_i,eps_j)]
              list_Bn.append(root)
         return list_Bn 
     
    def rootsCn(self, n):
         list_Cn = self.rootsAn(n)

         for i in range(0, n-1):
            for j in range(i+1,n-1): 
              root = [0]*i + [1]*(j-i) + [2]*(n-j-1) + [1] 
              list_Cn.append(root)
            root_2 = [0]*i + [2]*(n-i-1) + [1]
            list_Cn.append(root_2)
         return list_Cn        

    def rootsDn(self, n):
         list_Dn = []
         for i in range(0, n-1):             
            for j in range(i, n-1):
                root = [0]*i + [1]*(j-i) + [0]*(n-j-2) + [0,0]
                list_Dn.append(root) 
         for i in range(0, n-2):             
             #root_0= [0]*i + [1 for k in range(i+1, n-1)] 
             root_0 = [0]*i + [1]*(n-i-2)
             root = root_0 + [1, 0] 
             list_Dn.append(root) 
             root = root_0 + [0, 1] 
             list_Dn.append(root) 
             root = root_0 + [1, 1] 
             list_Dn.append(root) 
                     
         for i in range(0, n-2):
            for j in range(i+1,n-2):
                   root = [0]*i + [1]*(j-i) + [2]*(n-j-2) + [1,1] 
                   list_Dn.append(root)                    
         root = [0]*(n-1) + [1] 
         list_Dn.append(root)          
         root = [0]*(n-2) + [1] + [0]           
         list_Dn.append(root)          
         return list_Dn   

    def orderListOfRoots(self, rl):
      ht_max =  self.coxNumber ## = sum(self.maxRoot) + 1  
      dictByHeight = {}
      for root in rl:
          ht = sum(root)
          if ht in dictByHeight.keys():
             rlist_by_ht = dictByHeight[ht]
             rlist_by_ht.append(root)
          else:    
             rlist_by_ht = []
             rlist_by_ht.append(root)
             dictByHeight[ht] = rlist_by_ht
                      
      for ht in range(1, ht_max): 
         if ht in  dictByHeight.keys():
            rlist_by_ht = dictByHeight[ht] 
            rlist_by_ht.sort(reverse=True)
            for i in range(len(rlist_by_ht)):  
                self.rlist.append(rlist_by_ht[i])          
                
    def collectRoots(self):
       n = self.n ## len(self.maxRoot)
       if self.diagram == 'A':
          rl = self.rootsAn(n)
       elif self.diagram == 'B':
          rl = self.rootsBn(n)
       elif self.diagram == 'C':
          rl = self.rootsCn(n)
       elif self.diagram == 'D':
          rl = self.rootsDn(n)
       elif (self.diagram  == 'E' and n in (6,7,8)) or self.diagram  in ('F', 'G'):
          rl = erl.getExceptRootList(self.diagram, self.n)
       self.orderListOfRoots(rl) 
                                           
    def getRootlist(self):
        return self.rlist

    '''   ----------- Print Functions ------------- ''' 
    def printRoots(self):
        #print(*self.rlist, sep='\n')
        for i in range(len(self.rlist)): 
            if self.bVal == 1:
               print(i, ') ', self.rlist[i])
            else:
               sc = self.scalarSquare(self.rlist[i])
               print(i, ') ', self.rlist[i], ' ## sq.len: ', sc)
               
          
            
if __name__ == "__main__":   
     rs = PositiveRoots('D',4)
     #rs.printRoots()
     
     