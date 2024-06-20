#!/usr/bin/env python
# coding: utf-8

# In[713]:


#master_list_block  [number,divisors, multiples, occurrences of the number]
def master_list_block_generator():
    master_list_block = [0,[],[],0]
    return master_list_block


# In[719]:


#for each element in master list find multiples and divisor
def master_list_handler(l,master_list):
    
    if(len(master_list)) < 2:
        return 
    
    i = 1 #list_pointer
    j = 1 #list_pointer_reset
    for m_num in master_list:

        if m_num == master_list[-1]:
            break
        if m_num[0] > 599999:
            continue
        else:
            for num in l[i:]:  
                if num % m_num[0] == 0:
                    if( (len(m_num) == 0) ):
                        m_num[2].append(num)
                    elif ((m_num[-1] < num)):
                        m_num[2].append(num)

                        
                    if( (len(master_list[i][1]) == 0)):
                        master_list[i][1].append(num)
                    elif (master_list[i][1][-1] < num):
                        master_list[i][1].append(num)

                i += 1
                print(m_num)
            j += 1
            i = j


# In[715]:


#calculate the numbers of lucky triple:
def lt_calculator(master_list):
    counter = 0
    for item in master_list:
        if(item[3] >= 3):
            counter += 1
        if ((len(item[1]) == 0 ^ len(item[2]) == 0) and item[3] < 2):
            continue
        if ((len(item[1]) == 0 and len(item[2]) == 0)):
            continue
            
        else:
            if(((len(item[1]) == 0) ^ (len(item[2]) == 0)) and item[3] > 1):
                counter = counter + (max(len(item[1]),len(item[2])) * 1)
            else:
                counter = counter + (len(item[1]) * len(item[2]) * min(2,item[3]))
    return counter


# In[716]:


#calculate the numbers of lucky triple:
def lt_calculator2(master_list):
    counter = 0
    for item in master_list:
        if(item[3] >= 3):
            counter += 1
            
        if ((len(item[1]) == 0 or len(item[2]) == 0)):
            continue
            
        if(((len(item[1]) != 0) and (len(item[2]) != 0))):
                counter = counter + (max(len(item[1]),len(item[2])))
    return counter


# In[717]:


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


# In[718]:


def solution(l):
        master_list = []
        master_list = master_list_generator(l)
        master_list_handler(l,master_list)
        return lt_calculator(master_list)
        


# In[ ]:




