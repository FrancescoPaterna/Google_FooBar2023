#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Basic Script Solution no rep


# In[167]:


tester()


# In[159]:


def solution(l):
    
    master_list = []
    clt = '0'
    counter = 0
    a,b,c,i,j,k,p = 0,0,0,0,0,0,0
    ll = len(l)
    
    #case list with all same values (x,x,x,x...)
    for p in range(1,ll):
        if l[0] != l[i]:
            break;
        else:
            if i == ll - 1:
                return 1
    
    #case list too short
    if ll < 3:
        return 0
    
    #standard case
    while i < (ll-2):
        a = l[i]
        j = i + 1
        while j < (ll-1):
            b = l[j]
            if (b % a == 0 and b >= a):
                k = j + 1
                while k < ll:
                    c = l[k]
                    if (c % b == 0 and c >= b):
                        clt = ltg(a,b,c)
                        if clt not in master_list:
                            counter += 1
                            master_list.append(clt)
                        k += 1
                    else:
                        k += 1
                j += 1
            else:
                j += 1
        i += 1
    return counter
                        
#luck_triple_generator:
def ltg(x,y,z):
    return "a" + str(x) + "b" + str(y) + "c" + str(z)                    
                
        
        


# In[166]:


def tester():
    if (solution([1,1,2,2]) == 1):
        print("######## CORRECT ######## => TEST 1 ")
    else:
        print("======== FALSE ============> TEST 1 ", "EXPECTED ", 3, " RETURNED ",solution([1,1,2,2]))



# In[133]:


def calculator(x):
    y = x
    a = 0
    for i in range(1, x + 1):
        for i in range(1 , y + 1):
            a = a + i 
        y = y -1
    return a


# In[158]:





# In[134]:


calculator(3000)


# In[139]:


for i in range (2,100,2):
    print(i)


# In[ ]:




