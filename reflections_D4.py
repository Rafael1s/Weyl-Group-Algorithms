root_system = 'D4'

'''reflections_D4.tex'''

s1 = [[-1, 1, 0, 0],
      [ 0, 1, 0, 0],
      [ 0, 0, 1, 0],
      [ 0, 0, 0, 1]]

s2 = [[1, 0, 0, 0],
      [1,-1, 1, 1],
      [0, 0, 1, 0],
      [0, 0, 0, 1]]

s3 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 1,-1, 0],
      [0, 0, 0, 1]]

s4 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0,-1]]

refl = []
refl.append(s1)
refl.append(s2)
refl.append(s3)
refl.append(s4)

''' Cartan matrix '''
Cmatr = \
[[ 2,-1, 0, 0],
 [-1, 2,-1,-1],
 [ 0,-1, 2, 0],
 [ 0,-1, 0, 2]]
    
''' Let w0 denote the unique Weyl group element of maximum length. 
Length l(w0) is equal to the number of positive roots 
for the Weyl group W; Nlevels =  number of positive roots + 1'''

Nlevels = 13