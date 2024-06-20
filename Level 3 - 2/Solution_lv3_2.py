#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Markov Chain
from fractions import Fraction
from decimal import Decimal


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
    a = 2*len(matrix)
    P = matrix
    for i in range(0, a):
        P = matrix_product(P,P,len_m,len_m,len_m)
    
    return P
    

#least common divisor
def lcd(a, b):
    while b:
        a, b = b, a%b
    return a

#least common multiple
def lcm(a, b):
    return a // lcd(a, b) * b
        
        
#return the solution correctly parsed
def parse_row(final_row,ter):
    su = 0
    divisor = 0
    final = []
    fractions = []
    i = 2
    for el in ter:
        if final_row[el] != 0:
            fractions.append(converter(final_row[el]))
        else:
            fractions.append(Fraction(0))
            
    for el in fractions:
        if divisor == 0:
            divisor = el.denominator
            
        else:
            divisor = lcm (divisor,el.denominator)
     
    for el in fractions:
        if el.denominator == divisor:
            final.append(el.numerator)
        else:
            final.append(el.numerator*(divisor/el.denominator))
        
    final.append(divisor)
    return final
    
    
    
def fraction_extractor(num):
    z = 1.0/num
    a = int(z)
    b = (z) - int(z)
    
    if(b==0):
        return [a,'a']
    
    f = []
    f.append(a)
    
    for i in range(0,1):
        y = 1.0/b
        c = int(y)
        d = (1/y) - int (1/y)
        f.append(c)
        b=d 
    f.append('Q')
    return f
    
    

def loop(c,i):
    if c[i+1] == 'Q':
        return c[i]
    else:
        a = c[i]
        i += 1
        zed = a + Fraction(1,loop(c,i))
        return zed
        
        
def fraction_generator(c):
    if c[1] == 'a':
        return Fraction(1,c[0])
    else:
        i = 0
        f = Fraction(1,Fraction(loop(c,i)))
    return f
    
    
def repeating_decimal(sn):
    j = 0
    for i in range(0,5):
        sn[i:]
        nn = check_token(sn[i:])
        if nn != False:
            if j == 0:
                numerator = int(nn)
                denominator = int('9'*(len(nn)))
                return Fraction(numerator,denominator)
            else:
                
                numerator = int(sn[0:j]+ nn)- (int(sn[0:j]))
                denominator = int('9'*(len(nn)))*(10**j)
                
                #print("PERIODICO CON DISTACCO - NUMERO PERIODICO",nn , " DISTACCO DI ", j)
                #print(numerator,denominator)

                
                #return Fraction(int(sn[0:j]+ nn)-(int(sn[0:j]+ nn)//(10**(len(nn)-j+1))),int('9'*(len(nn)-j+1))*(10**j))
                return Fraction(numerator,denominator)
        j += 1
    return False
    
#convert decimal to fraction:
def converter(dec):
    flag = False
    dk = int(dec)
    strx = str("{0:.16f}".format(dec))
    if strx[2] == '0':
        flag = 0
        for i in range(2,18):
            if strx[i] == '0':
                flag += 1
            else:
                break
                
    
    #limited decimal
    if strx[-4:] == "0000" and dk == 0:
        return Fraction(int(strx[2:]),10**(len(strx)-2))
            
    intd = int(dec*(10**15))
    if(flag != False):
        sn = '0'*flag+str(intd)
        sn[0:-1]
    else:
        sn = str(intd)[0:-1]

    #illimited decimal with repetition
    rd = repeating_decimal(sn)
    
    if rd != False:
        return rd

    else:
        #illimited decimal with repetition
        ff = fraction_generator(fraction_extractor(dec))
        if ff.denominator <= 2147483647:
            return fraction_generator(fraction_extractor(dec))
        else:
            return shittyalg(dec)
            

def shittyalg(dec):
    for i in range(49,20000):
        b = "{0:.10f}".format(dec * i)
        if int(str(b[0:1])) == 1:
            return Fraction(1,i)
        
def check_token(s):
    OUT = ""
    lens = len(s)
    lax = lens/2
    if s == s[0]*len(s):
        return s[0]
    else:
        for i in range(2,lax+1):
            ii = i + 1
            iii = i + 2
            A = s[0:i]
            B = s[i:i+i]
            if ((B == A)and find_num_substrings(s,A) >= lens//len(A)):
                if len(OUT)<len(A):
                    if len(OUT) == 0:
                        OUT = A
                    elif OUT*(len(A)/len(OUT)) not in A:
                        OUT = A
                        

    if len(OUT) > 0 :
        return OUT
    else:
        return False


# In[16]:


#find the number of occurrences of a substring
def find_num_substrings(string, substring):
    indices = []
    i = 0
    counter = 0
    while i < len(string):
        j = string.find(substring, i)
        if j == -1:
            break
        counter += 1
        i = j + len(substring)
    return counter
    

    
def solution(matrix):
    terminal_state = []
    len_m = len(matrix)
    for i in range(1,len_m):
        if(check_terminal_state(matrix[i],i)== True):
            terminal_state.append(i)
    T = []
    T = transition_matrix(matrix)
    T = calculate_probability_matrix(T,len_m)
    return parse_row(T[0],terminal_state)
            


# In[ ]:




