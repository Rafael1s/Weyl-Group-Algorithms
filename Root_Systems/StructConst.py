''' developed by Rafael Stekolshchik. 30-oct-2024 '''

from RootLength import RootLength as rlen
from Extrasp import Extraspecials as extr

import numpy as np

class StructConst(object):
    def __init__(self, diagram, n):
       self.diagram = diagram 
       self.extr = extr(self.diagram, n)
       self.rlen = rlen(self.diagram, n)
       self.initNabVal = -999.0   
       self.getIndSum = self.extr.getIndSum
       self.scalarSquare = self.rlen.scalarSquare
       self.indexOfRoot = self.extr.pr.indexOfRoot
       self.rlist = self.extr.pr.getRootlist()
       self.dim = len(self.rlist) 
       self.matr_Nab_pairs = np.full((self.dim,self.dim), self.initNabVal)   
       self.matr_Nab_aPos_bNeg = np.full((self.dim,self.dim), self.initNabVal)
       self.dictNabExrasp = self.extr.getDictNabExrasp()
       self.dictTheSameSums= self.extr.getDictTheSameSums()
       self.getNabForAllPairs()   ## a,b positive
       self.getNabForAllPairs_aPos_bNeg()
       
    def fillNab(self, i, j, Nab): 
        self.matr_Nab_pairs[i][j] = Nab
        self.matr_Nab_pairs[j][i] = -Nab   
        
    def getExtraspPair(self, isum):
        pairs_same_sum = self.dictTheSameSums[isum] 
        return pairs_same_sum[0]
    
    def isExtrasp(self, i,j):
        isum = self.getIndSum(i,j)
        if isum in self.dictNabExrasp.keys():
            pairs = self.dictTheSameSums[isum]
            if pairs[0] == [i,j]:
               return isum
            else:
               return -1 
        else:
            return -1 
            
    ''' rlist[i]  and rlist[j] both are positive roots '''                          
    def getNabForAllPairs(self):
      if self.diagram != 'F':  
        for i in range(len(self.rlist)):
           for j in range(i+1, len(self.rlist)):    
               isum  = self.isExtrasp(i,j)
               if isum  != -1: ## i.e., this  is extrasp
                  Nab = self.dictNabExrasp[isum]                       
               else:
                  Nab = self.calcNab(i,j) 
               self.fillNab(i,j, Nab) 
      else: ## diagram is 'F'
        for i in range(len(self.rlist)):
           for j in range(i+1, len(self.rlist)):    
               isum  = self.isExtrasp(i,j)
               if isum  != -1: ## i.e., this  is extrasp
                  Nab = self.dictNabExrasp[isum]                       
               else:
                  Nab = self.calcNab_F4(i,j) 
               self.fillNab(i,j, Nab) 
          
      for i in range(len(self.rlist)):
            self.fillNab(i,i, 0)   
       
    ''' Version for full formula, including F4 '''                                  
    def calcNab_F4(self, r,s):        
          Nab = self.matr_Nab_pairs[r][s]  
          #print('Nab = ', Nab, ', r = ', r, 's = ', s)                  
          if Nab != self.initNabVal:
              return Nab
        
          isum = self.getIndSum(r,s)
          if isum == -1:
              self.fillNab(r,s,0)
              return 0
          
          sc_r_pl_s = self.scalarSquare(self.rlist[isum])           
          r1,s1 = self.getExtraspPair(isum)
          
          if r1 == -1 and s1 ==  -1:
              return 0
          
          N_s1r1 = self.matr_Nab_pairs[r1][s1] 

          if r1 == r and s1 == s:
              return self.fillNab(r,s,N_s1r1) 
          elif r1 == s and s1 == r :
              return self.fillNab(r,s,-N_s1r1) 
          
          ## Now we have (r1,s1) and (r,s), N(r1,s1) = 1 
          ##    Find  N1, N2, N3, N4 

          N1, N2 = 0, 0
          s_min_r1 = [x - y for x,y in zip(self.rlist[s], self.rlist[r1])] 
          ind_s_min_r1 = self.indexOfRoot(s_min_r1)  
          if ind_s_min_r1 != -1:    
             sq_s_min_r1 = self.scalarSquare(s_min_r1)
             sq_s = self.scalarSquare(self.rlist[s])
             sq_s1 = self.scalarSquare(self.rlist[s1])
             N1 = sq_s_min_r1*self.calcNab_F4(ind_s_min_r1, r1)/sq_s             
             N2 = self.calcNab_F4(ind_s_min_r1, r) /sq_s1
          
          N1xN2 = N1*N2  
          N3, N4 = 0,0
          
          r_min_r1 = [x - y for x,y in zip(self.rlist[r], self.rlist[r1])]
          ind_r_min_r1 = self.indexOfRoot(r_min_r1)  
          if ind_r_min_r1 != -1:    
              sq_r_min_r1 = self.scalarSquare(r_min_r1)
              sq_r = self.scalarSquare(self.rlist[r])
              sq_s1 = self.scalarSquare(self.rlist[s1])
              N3 = sq_r_min_r1*self.calcNab_F4(r1, ind_r_min_r1)/sq_r
              N4 = self.calcNab_F4(ind_r_min_r1, s)/sq_s1
          
          N3xN4 = N3*N4
          Nab = (N1xN2 + N3xN4)*sc_r_pl_s/N_s1r1
          return Nab    
      
    def calcNab(self, r,s):        
          Nab = self.matr_Nab_pairs[r][s]                    
          if Nab != self.initNabVal:
              return Nab
        
          isum = self.getIndSum(r,s)
          if isum == -1:
              self.fillNab(r,s,0)
              return 0
          
          r1,s1 = self.getExtraspPair(isum)
          
          if r1 == -1 and s1 ==  -1:
              return 0
          
          N_s1r1 = self.matr_Nab_pairs[r1][s1] 

          if r1 == r and s1 == s:
              return self.fillNab(r,s,N_s1r1) 
          elif r1 == s and s1 == r :
              return self.fillNab(r,s,-N_s1r1) 
          
          N1, N2, N3, N4 = 0, 0, 0, 0
          s_min_r1 = [x - y for x,y in zip(self.rlist[s], self.rlist[r1])] 
          ind_s_min_r1 = self.indexOfRoot(s_min_r1)  
          if ind_s_min_r1 != -1:    
             N1 = self.calcNab(ind_s_min_r1, r1)             
             N2 = self.calcNab(ind_s_min_r1, r) 
          
          r_min_r1 = [x - y for x,y in zip(self.rlist[r], self.rlist[r1])]
          ind_r_min_r1 = self.indexOfRoot(r_min_r1)  
          if ind_r_min_r1 != -1:    
              N3 = self.calcNab(r1, ind_r_min_r1)
              N4 = self.calcNab(ind_r_min_r1, s)
          
          Nab = (N1*N2 + N3*N4  )/N_s1r1
          if self.diagram == 'C':
             sq_s1 = self.scalarSquare(self.rlist[s1])
             sc_r_pl_s = self.scalarSquare(self.rlist[isum])           
             Nab = Nab*sc_r_pl_s/sq_s1
             
          return Nab
    
                                           
    def replace(self, i):
       if i >= 0:
          return ' ' + str(i)
       else:
          return str(i)
             
    
    '''========  Cases where one of roots is negative =========== '''
    
    def isRoot_PosOrNeg(self, root):
        for i in range(len(root)):
           if root[i] > 0:
              return 1
           elif root[i] < 0:
              return -1
        
    def getRoot_a_plus_b(self, i, j):
        
         #print('a_plus_b = ',a_plus_b)           
         root_a_pos, root_b_neg = self.rlist[i], self.rlist[j]
         ##root_b_neg = self.rlist[j]
         a_plus_b = [x - y for x,y in zip(root_a_pos, root_b_neg)]
         sign_a_plus_b = self.isRoot_PosOrNeg(a_plus_b)
         
         isum = -1
         if sign_a_plus_b > 0:
             isum = self.indexOfRoot(a_plus_b)  
         elif sign_a_plus_b  < 0:
             opposite =  [-x  for x in a_plus_b]
             isum = self.indexOfRoot(opposite)
         if isum != -1: 
            return isum, a_plus_b, sign_a_plus_b
         else:
            return -1, -1, -1
             
    '''  rlist[i] and -rlist[j] '''    
    def buildNab_OnePair_aPos_bNeg(self, i, j):

        ''' Here i < j '''
        isum, a_plus_b, sign_a_plus_b = self.getRoot_a_plus_b(i, j)
        #print(' isum, a_plus_b, sign_a_plus_b: ',  isum, a_plus_b, sign_a_plus_b)
        if isum == -1:
            self.matr_Nab_aPos_bNeg[i][j] = 0
            self.matr_Nab_aPos_bNeg[j][i] = 0
        else: 
            Nab = self.calcNab_aPos_bNeg(i, j, isum, a_plus_b, sign_a_plus_b)
            self.matr_Nab_aPos_bNeg[i][j] = Nab
            self.matr_Nab_aPos_bNeg[j][i] = -Nab
            ##print('1: root_a, root_b = ', self.rlist[i], self.rlist[j], ', Nab = ', Nab)
                            
    ''' Here a > 0, b < 0 '''        
    def calcNab_aPos_bNeg(self, i, j, isum, a_plus_b, sign_a_plus_b):
         root_a, root_b = self.rlist[i], self.rlist[j]         
         sq_a_plus_b  = self.scalarSquare(a_plus_b)
         if sign_a_plus_b > 0:
             ''' bNeg = -rlist[j], ## self.calcNab(isum, j),  formula (2.11) '''
             Ncb =  self.matr_Nab_pairs[isum][j]
             sq_a = self.scalarSquare(root_a)
             return Ncb*sq_a_plus_b/sq_a
             
         elif sign_a_plus_b < 0:
             ''' self.calcNab(isum, i),  formula (2.12)  '''
             Nca =  self.matr_Nab_pairs[isum][i]
             sq_b = self.scalarSquare(root_b)
             return  Nca*sq_a_plus_b/sq_b
         
         
    def getNabForAllPairs_aPos_bNeg(self):
                
        for i in range(len(self.rlist)):
           for j in range(i, len(self.rlist)):
               if i == j:
                   self.matr_Nab_aPos_bNeg[i][j] = 0
                   self.matr_Nab_aPos_bNeg[j][j] = 0
               else:                   
                   ''' Here,  i < j '''
                   self.buildNab_OnePair_aPos_bNeg(i, j) 
                 
    def getNij(self, i, j):
        if abs(i) > len(self.rlist) - 1:
            print('ERROR: Abs.value of ', i, ' > ', len(self.rlist) - 1)
            return
        
        if abs(j) > len(self.rlist) - 1:
            print('ERROR: Abs.value of ', j, ' > ', len(self.rlist) - 1)
            return
        
        ''' i < 0 and j > 0:  ##  Formulala (2.4) 
            i < 0 and j < 0:  ##  Formulala (2.1)   '''
        if i > 0  and j > 0:
            return self.matr_Nab_pairs[i][j] 
        elif i > 0 and j < 0:
            #j1 = abs(j)
            #print('i, j1: ', i, j1)
            return self.matr_Nab_aPos_bNeg[i][abs(j)]  
        elif i < 0 and j > 0: 
            v = self.matr_Nab_aPos_bNeg[j][abs(i)]           
            return -v
        elif i < 0 and j < 0:  
            v = self.matr_Nab_pairs[abs(j)][abs(i)] 
            return -v
        
    def getNab(self, root_a, root_b):   

        try:
          if self.isRoot_PosOrNeg(root_a) == 1:
              i = self.rlist.index(root_a) 
          else:
              oppos_a = [-x for x  in root_a]
              i = -self.rlist.index(oppos_a)               
        except:  
          print('ERROR: ', root_a, ' is not a root')
          return

        try:
          if self.isRoot_PosOrNeg(root_b) == 1:
              j = self.rlist.index(root_b)        
          else:    
              oppos_b = [-x for x  in root_b]
              j = -self.rlist.index(oppos_b)               
        except:  
          print('ERROR: ', root_b, ' is not a root')
          return
        
        Nab = self.getNij(i, j)
        return Nab
                 
            
if __name__ == "__main__":    
    
    st_cnst = StructConst('C', 6)
    
    ''' ------------- Interface getNij -------------------- '''
    ''' getNij, Test 1:  root iindex out of range'''
    st_cnst.getNij(36, 1)
    st_cnst.getNij(6, 38)
    
    ''' getNij, Test 2:  two positive roots'''
    Nab = st_cnst.getNij(3, 2)
    print('getNij: N(r3, r2) = ', Nab)

    ''' getNij, Test 3   positive and negative '''
    Nab = st_cnst.getNij(7, -1)
    print('getNij: N(r7, -r1) = ', Nab)

    ''' getNij, Test 4  negative and positive'''    
    Nab = st_cnst.getNij(-6, 1)
    print('getNij: N(-r6, r1) = ', Nab)

    ''' getNij, Test 5  two negative roots '''    
    Nab = st_cnst.getNij(6, 2)
    print('getNij: N(-r6, -r2) = ', Nab)
    
    ''' ------------ Interface getNab ------------------- '''
    ''' getNab , Test 1 first vector is not a root'''
    root_a = [0, 0, 3, -1, 0, 0]
    root_b = [0, 1, 0, 0, 0, 0]
    Nab = st_cnst.getNab(root_a, root_b)
    ''' getNab second vector is not a root'''
    root_a = [0, 1, 0, 0, 0, 0]
    root_b = [0, 0, 2, -1, 0, 0]
    Nab = st_cnst.getNab(root_a, root_b)

    ''' getNab, Test 2 '''
    root_a = [0, 0, 0, 1, 0, 0]
    root_b = [0, 0, 1, 0, 0, 0]
    Nab = st_cnst.getNab(root_a, root_b)
    print('getNab: N(r3, r2) = ', Nab)

    ''' getNab, Test 3 '''
    root_a = [0, 1, 1, 0, 0, 0]
    root_b = [0, -1, 0, 0, 0, 0]
    Nab = st_cnst.getNab(root_a, root_b)
    print('getNab: N(r7, -r1) = ', Nab)

    ''' getNab, Test 4 '''
    root_a = [-1, -1, 0, 0, 0, 0]
    root_b = [0, 1, 0, 0, 0, 0]
    Nab = st_cnst.getNab(root_a, root_b)
    print('getNab: N(-r6, r1) = ', Nab)

    ''' getNab, Tets 5 '''
    root_a = [-1, -1, 0, 0, 0, 0]
    root_b = [0, 0, -1, 0, 0, 0]
    Nab = st_cnst.getNab(root_a, root_b)
    print('getNab: N(-r6, -r2) = ', Nab)
