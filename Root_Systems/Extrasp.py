''' developed by Rafael Stekolshchik. 30-oct-2024 '''

from PositiveRoots import PositiveRoots as pr

class Extraspecials(object):
    def __init__(self, diagram, n):        
       self.diagram = diagram 
       self.pr = pr(diagram, n)
       self.indexOfRoot = self.pr.indexOfRoot
       self.rlist = self.pr.getRootlist()
       self.dictNabExrasp = {}
       self.dictTheSameSums= {}
       self.constructDictTheSameSums()
                             
    def getIndSum(self, i,j):
        vec_ij = [x + y for x,y in zip(self.rlist[i], self.rlist[j])]
        return self.indexOfRoot(vec_ij)
 
    def getNabForExtrasp(self, i,j):
        isum = self.getIndSum(i,j)
        if isum !=-1:
           ri_min_rj = [x - y for x,y in zip(self.rlist[i], self.rlist[j])]
           if self.indexOfRoot(ri_min_rj) == -1:
               return 1
           else: ## Here, ri_min_rj is root 
              ri_min_2rj = [x - 2*y for x,y in zip(self.rlist[i], self.rlist[j])]           
              if self.indexOfRoot(ri_min_2rj) == -1: 
                   return 2
              else: ## Here, ri_min_rj and ri_min_2rj are roots 
                 ri_min_3rj = [x - 3*y for x,y in zip(self.rlist[i], self.rlist[j])]           
                 if self.indexOfRoot(ri_min_3rj)  == -1:
                       return 3
        else:     
           return -1
       
                   
    def constructDictTheSameSums(self):
      for i in range(len(self.rlist)):
        for j in range(i+1, len(self.rlist)):
           isum = self.getIndSum(i,j)
           if isum != -1: 
              if isum in self.dictTheSameSums.keys():
                   pairs_same_sum = self.dictTheSameSums[isum]  
                   pairs_same_sum.append([i,j])
              else: 
                   ''' This pair [i,j] is extraspecial ! '''
                   pairs_same_sum = []
                   pairs_same_sum.append([i,j])
                   self.dictTheSameSums[isum] = pairs_same_sum
                   self.dictNabExrasp[isum] = self.getNabForExtrasp(j,i) 
                                                     
    ''' ----------------  Get Functions ---------------  '''    

    def getDictTheSameSums(self):
        return self.dictTheSameSums
    
    def getDictNabExrasp(self):
        return self.dictNabExrasp
            
    '''  -----------  Functions in Extraspecial ---------'''    
                                                                                              
    def printExtrasp(self):
        k = 0
        for isum in self.dictNabExrasp.keys():
            pairs_same_sum = self.dictTheSameSums[isum]
            i,j = pairs_same_sum[0]
            Nab = self.dictNabExrasp[isum]
            k += 1
            print(k, ') ', i, j, ', isum: ', isum, ', N(i,j): ', Nab)            
               
    def printCarterQuartets(self):
        k = 0
        for isum in self.dictNabExrasp.keys():
            pairs_same_sum = self.dictTheSameSums[isum]
            r1,s1 = pairs_same_sum[0]
            #Nab = self.dictNabExrasp[isum]
            for ipr in range(1, len(pairs_same_sum)):
                pair = pairs_same_sum[ipr]
                k += 1
                r,s = pair[0], pair[1]
                s_min_r1 = [x - y for x,y in zip(self.rlist[s], self.rlist[r1])]
                r_min_r1 = [x - y for x,y in zip(self.rlist[r], self.rlist[r1])]
                ind_s_min_r1 = self.indexOfRoot(s_min_r1)
                ind_r_min_r1 = self.indexOfRoot(r_min_r1)
                print(k, ')  r1, r, s, s1 = [', r1, r,s, s1, '],  sum = ', isum,
                     ', s-r1, r-r1 = ', ind_s_min_r1, ind_r_min_r1)
                             
       
if __name__ == "__main__":    
    extr = Extraspecials('C',6)
    extr.printExtrasp()
    extr.printCarterQuartets() 
  


