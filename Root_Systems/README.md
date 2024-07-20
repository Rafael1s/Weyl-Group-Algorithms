#  Root systems associated with Lie algebras

* File __exc_root_list.py__ contains 5 lists of positive roots for exceptional root systems:
  E6, E7, E8, F4, G2.  The function __getExceptRootList(diagram, n)__ returns the corresponding root list
  The parameter __diagram__ can be one from 3 characters {'E', 'F', 'G'}, and the parameter __n__ takes values
  6, 7, 8 for the case 'E'.  For cases 'F', 'G' __n__ should be any positive integer number, doesn't matter what.
  The output list is the list of positive roots ordered in the __regular ordereing__. Acoocrding the
  regular ordereng roots are ordred by height. In the case of the same height they are ordered in the lexicographical
  ordering. For example, for **G2** the output root list is as follows:
  
![](imgs/G2_root_list.png)

   For **F4** the output root list contains **24** roots.
   For **E6** (resp, **E7**, resp. **E8**) the output root list contains **36** (resp. **63**, resp. **120** roots)

*  File __CoxeterNumber.py__ contains only one function __getCoxeterNumber(diagram, n)__.
   Here, diagram is one from 7 characters: {'A', 'B', 'C', 'D', E', 'F', 'G'}.  The paramter __n__ should be only
   for diagram 'E', n = 6,7,8. This function returns  the Coxeter number, which coincides with the height  of the
   maximal root (increased by 1) for the corresponding root system. This number is used in the file
   __PositiveRoots.py__ to loop throgh he height of the roots.

*  File __BilinearForm.py__ contains the matrices of bilinear form for all types of root system. For the exceptional types
   __E, F, G__  these matrices are specified explicitly, whereas for serias types they are implicitly given, namely they are
   given by some short functions. These function for series __B, C, D__ just update a few elements of the matrix for the
   serias __A__.  For example, for series __C__ this function is as follows:

   ![](imgs/getBn_getCn.jpg)

   This file provides function __getBilForm(diagram, n)__ , where parameters __diagram__ nad __n__ are as in the previous 
   paragraphs. The output of the function __getBilForm__ is the matrix of the bilinear form. For example, the matrices
   of the bilnear form for cases __B5__ and __C5__ are aa follows: 
   
   ![](imgs/matr_B5_C5.JPG)

* File MaximalRoot.py provides the maximal positive root for all cases Root Systems. The main function is
   __getMaxRoot(diagram, n)__.  Parameters __diagram__ nad __n__ are as in the previous paragraphs.

* File __PositiveRoots.py__  contains class  __class PositiveRoots__ which provides the list of positive roots for any class
  of root system. For exceptional root systems __E, F, G__  lists of positive roots are provided by the file __exc_root_list.py__,
  see above.  For series types __A, B, C, D__ the positive roots are obtained by some short functions. To use this class
  you need to call two lines like this:

     __rs = PositiveRoots('D',12)__
  
     __list_pos_roots = rs.getRootList()__ 
     
  
  
     


  
  
   
