#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import floor
def sum_of_floor_sqrt_2(start, end):
    result = 0
    for i in range(start, end + 1):
        result += math.floor(i * math.sqrt(2))
        print(math.floor(i * math.sqrt(2)))
    return int(result)



# In[2]:


def gauss(n):
    return n*(n+1)/2


# In[3]:


def graham(n):
    a = floor(n**(0.5))
    b = n*a
    c = (1.0/3) * (a**3)
    d = (1.0/2) * (a**2)
    e = (1.0/6) * (a)
    print(a,b,c,d,e)
    return int(b-c-d-e)


# In[4]:


def solution(s):
    return graham(s)


# In[5]:


graham((77))


# In[6]:


412*(2**0.5)**2


# In[7]:


77 ** (0.5)


# In[8]:


77**(0.5)


# In[9]:


float(1/3)


# In[10]:


4208-3003


# In[11]:


(77**2)/2


# In[143]:


4208-2964


# In[ ]:




