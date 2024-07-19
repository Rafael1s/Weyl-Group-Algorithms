

def getCoxeterNumber(diagram, n):
    if diagram == 'E': 
        if  n == 6:
            return 12
        elif n == 7: 
            return 18    
        elif n == 8:
            return 30
    elif diagram == 'F':
            return 12   
    elif diagram == 'G':
            return 6
    elif diagram == 'A':
            return n+1 
    elif diagram == 'B' or diagram == 'C': 
            return 2*n
    elif diagram == 'D':
            return 2*n-2
             
