#!/usr/bin/env python
# coding: utf-8

# In[2]:


import itertools

#bellmanford algorithm
def bellmanford(m,lm):
    
        dst = lm-1
        src = 0
        prices = [float("inf")] * lm
        prices[src] = 0

        
        for i in range(0,lm):
            tmpPrices = list(prices)
            
            for s in range(0,lm):
                for d in range(0,lm):
                    if prices[s] == float("inf") or s == d:
                        continue
                    if prices[s] + m[s][d] < tmpPrices[d]:
                        tmpPrices[d] = prices[s] + m[s][d]
            

            if prices != tmpPrices:
                #negative cycle case 
                if i == dst:
                    return 'False'
                #update current_best_path
                else:
                    prices = tmpPrices

            else:
                #end of bellmanford
                return prices[dst]

#generate path from a permutation             
def path_generator(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i-1], perm[i]))
    return path




def solution(times, time_limit):
    
    #Avoid bad input traps
    if time_limit > 999 or time_limit < 0:
        return []
    
    lm = len(times)
    dst = lm-1
    bunnies = lm -2
    
    #no bunnies to save :(
    if lm < 3:
        return []
    
    ##########################################################
    #BELLMAN FORD SCREENING
    
    #run bellman-ford algorithm
    res_bell = bellmanford(times,lm)
    
    #no escape case
    if res_bell == float("inf"):
        return []
    
    #negative cycle case
    elif res_bell == 'False':
        return [0,1,2,3,4][0:dst-1]

    #no enough time to escape case
    if res_bell > time_limit:
        return []
        
    ##########################################################
    # Update times cell with the shortest way to reach position
    # Floyd-Warshall Algorithm
    
    for k in range(lm):
        for i in range(lm):
            for j in range(lm):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]
    
    
    ##########################################################
    # SEE ALL POSSIBLE PATH
    
    #trying all the combination of bunnies from the largest
    #to the smallest
    for i in reversed(range(lm)):
        for perm in itertools.permutations(range(1,bunnies+1),i):
            current_time = 0
            #generate all the paths
            path = path_generator(perm)
            for s,e in path:
                #check if the time respect the time limit
                current_time += times[s][e]
                #if respects the time limit, return the bunnies
            if current_time <= time_limit:
                sol = list(perm)
                sol.sort()
                for i in range(len(sol)):
                    sol[i] -= 1
                return sol

    ##########################################################
    
    #no bunnies :(
    return []


# In[ ]:




