#TODO: Calculate the matrix of probability with eigenvectors
#TODO: Fix The Fraction generator to avoid lovely loops with my fantastic while == True :P
#4/10 for now, wow, such engineer, great coder, time to eat Pizza :3, see u 2night with a proper solution



#If a row has all 0 elements it is the row of a terminal state 
def check_terminal_state(row,i):
    for el in row:
        if el != 0:
            return False 
    #add Identity to the final state (ex s5 -> s5)
    row[i] = 1
    return True
    
#A simple function for the matrix_product (cr = len(A), b = len(B), cc = len(B[0]))
def matrix_product(A,B,cr,cc,b):
    C = []
    c_row = []
    cell = 0
    
    for i in range (0,cr):
        for j in range (0,cc):
            for k in range (0,b):
                cell = cell + (A[i][k] * B[k][j])
            c_row.append(cell)
            cell = 0
        C.append(c_row)
        c_row = []
    
    return C
            
                
#Generate the transition Matrix
def transition_matrix(m):
    i = len(m[0])
    j = len (m)
    if i != j:
        print("FATAL ERROR; not a square matrix!")
    divisor = 0.0
        
    
    for row in range(0,j):
        for col in range(0,j):
            divisor = divisor + m[row][col]
        for col in range(0,j):
            if divisor == 0:
                continue
            m[row][col] = m[row][col] / divisor
        divisor = 0.0
    
    return m
    
    
#Yes I know, With eigenvector is better, but without numpy, 
#if A^n works, why reinvent the whell?
def calculate_probability_matrix(matrix,len_m):
    a = 2 * len(matrix)
    P = matrix
    for i in range(0, a):
        P = matrix_product(P,P,len_m,len_m,len_m)
    
    return P
    
    
#return the solution correctly parsed
def parse_row(final_row,ter):
    su = 0
    divisor = 0
    final = []
    i = 2
    for el in ter:
        #print(ter)
        if final_row[el] != 0:
            while True:
                #print(round((final_row[el] * i - (final_row[el]*i // 1)),4), "AND ",i)
                if str(round((final_row[el] * i - (final_row[el]*i // 1)),4)) == '0.0':
                    if(divisor == 0 or i > divisor):
                        divisor = i
                    break
                i += 1
            i = 2
        
    for el in ter:
        final.append(int(final_row[el] * divisor))
                     
        
    final.append(divisor)
    return final
    
    
    
def solution(matrix):
    terminal_state = []
    len_m = len(matrix)
    for i in range(0,len_m):
        if(check_terminal_state(matrix[i],i)== True):
            terminal_state.append(i)
    T = []
    T = transition_matrix(matrix)
    T = calculate_probability_matrix(T,len_m)
    return parse_row(T[0],terminal_state)
        
        
        
    
