#!/usr/bin/env python
# coding: utf-8

# In[62]:


#master_list_block  [number,divisors, multiples, occurrences of the number]
def master_list_block_generator():
    master_list_block = [0,[],[],0]
    return master_list_block


# In[80]:


#generate a master list, this function complete just the section 0 and 3 of each master_block
def master_list_generator(l):
    ml = []
    j = 0
    for i in l:
        ml.append(master_list_block_generator())
        ml[j][0] = i
        ml[j][3] = 1
        j += 1
    return ml


# In[81]:


#for each element in master list find multiples and divisor
def master_list_handler(l,master_list):
    
    if(len(master_list)) < 2:
        return 
    
    i = 1 #list_pointer
    j = 1 #list_pointer_reset
    k = 0
    for m_num in master_list:
        if m_num[0] > 499999:
            continue;
        else:
            for num in l[i:]:
                if num == m_num[0]:
                    m_num[3] += 1
                    i += 1
                    continue
                if num % m_num[0] == 0:
                    m_num[2].append(num)
                    master_list[i][1].append(m_num[0])
                i += 1
        j += 1
        i = j


# In[82]:


#luck_triple_generator:
def ltg(x,y,z):
    return "a" + str(x) + "b" + str(y) + "c" + str(z)
    


# In[101]:


#calculate the numbers of lucky triple:
def lt_calculator(master_list):
    print(master_list)
    counter = 0
    for item in master_list:
        #case (y,y,y)
        if(item[3] == 3):
            counter += 1
        if(item[3] > 3):
            counter += counter + item[3] - 2
            
        #no enough occurences of the number for (x,x,y) or (y,x,x)
        if ((len(item[1]) == 0 ^ len(item[2]) == 0) and item[3] < 2):
            continue
            
        #case no multiples and no divisor, in the triple (x,y,z) the current number
        #cannot be an y number
        if ((len(item[1]) == 0 and len(item[2]) == 0)):
            continue
            
        else:
            #case (x,x,y) or (y,x,x)
            if(((len(item[1]) == 0) ^ (len(item[2]) == 0)) and item[3] > 2):
                if (len(item[2]) == 0):
                    for n in item[1]:
                        a = item[1].count(n)
                        if a < 3:
                            counter += 1
                        if a > 3:
                            counter = counter + a - 2
                elif (len(item[1]) == 0):
                    for n in item[2]:
                        a = item[2].count(n)
                        if a < 3:
                            counter += 1
                        if a > 3:
                            counter = counter + a - 2
            #case (x,y,z)
            elif(((len(item[1]) != 0) and (len(item[2]) != 0))):
                for x in item[1]:
                    a = item[1].count(n)
                    if a < 3:
                        bb = 1
                    if a > 3:
                        bb = sum3(a)
                for z in item[2]:
                    a = item[1].count(n)
                    if a < 3:
                        counter == counter + 1*bb
                    if a > 3:
                        counter = sum3(a) * bb
                            
    return counter


# In[102]:



def solution(l):
        master_list = []
        master_list = master_list_generator(l)
        master_list_handler(l,master_list)
        sol = lt_calculator(master_list)
        return sol
        


# In[105]:


solution([1,2,1,1,1,1,2])


# In[73]:


#9    3++6


# In[ ]:


a,b,c,d,2

a,b,2

a,c,2
b,c,2

a,d,2
b,d,2
c,d,2

a,b,c,d,e,2

a,e
b,e
c,e
d,e


# In[57]:


def sum3(a):
    i = a + 1
    k = 1
    j = 2
    for i in range (2,a):
        k = k + 1*j
        j += 1
    return k
            
    


# In[75]:


sum3(4)


# In[ ]:




