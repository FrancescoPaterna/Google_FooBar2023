#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Dynamic Programming - Bottom Up Solution

from math import log

def solution(mach,facula):
    m = int(mach)
    f = int(facula)
    counter = 0
    g = False
    
    #Corner Case (1,1)
    if (m == f == 1):
        return '0'
    
    #Corner Case (0,0) (x,0) (0,y) (x,x) or negative numbers
    if(m <= 0 or f <= 0 or m == f):
        return "impossible"
     
    #Corner Case two multiple numbers (x,n*x) (n*y,y) with n,y != 1
    if(min(m,f) != 1 and (m%f == 0 or f%m == 0)):
        return "impossible"
    
    
    #Subtract the largest value with the smallest until the solution is reached
    while(m > 0 and f > 0):
        #print(m,f)
    
        #gap check (Ex. m = 99, n = 999999999999999)
        if min(m,f) != 1:
            g = fixer(m,f)
            
        if (g != False):
            counter = counter + g
            if (m > f):
                m = m - (f * g)
                g = False

                #print(m)
                
            else:
                f = f - (m * g)
                g = False
                
                
        #Corner Case, both even
        if(m%2 == f%2 == 0):
            return "impossible"
    
        #Corner Case (x,1) (1,y)
        if (m != f and min(m,f) == 1):
            return str(counter + (max(m,f) -1))
            
        if(m == f == 1):
            return str(counter) 
                
        if(m < f):
            f = f - m
        elif(m > f):
            m = m - f
        else:
            return "impossible"
        
        counter += 1
        
        
        if(m == f == 1):
            return str(counter) 
        
           
    return "impossible"
    
#speeds up the process in case of a large gap between the two numbers (exponential gap)
def fixer(a,b):
    a = max(a,b) // min(a,b)
    if a <= 1:
        return False
    else:
        return a


# In[ ]:




