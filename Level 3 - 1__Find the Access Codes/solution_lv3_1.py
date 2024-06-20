#master_list_block  [number,divisors, multiples, occurrences of the number]
def master_list_block_generator():
    master_list_block = [0,[],[]]
    return master_list_block



#generate a master list, this function complete just the section 0 and 3 of each master_block
def master_list_generator(l):
    ml = []
    j = 0
    for i in l:
        ml.append(master_list_block_generator())
        ml[j][0] = i
        j += 1
    return ml



#for each element in master list find multiples and divisor
def master_list_handler(l,master_list):
    
    if(len(master_list)) < 2:
        return 0
    
    i = 1 #list_pointer
    j = 1 #list_pointer_reset
    k = 0
    for m_num in master_list:
        for num in l[i:]:
            if num % m_num[0] == 0:
                m_num[2].append(num)
                master_list[i][1].append(m_num[0])
            i += 1
        j += 1
        i = j






#calculate the numbers of lucky triple:
def lt_calculator(master_list):
    counter = 0
    for item in master_list:
            if(((len(item[1]) != 0) and (len(item[2]) != 0))):
                counter = counter + (len(item[1]) * len(item[2]))
              
                            
    return counter





def solution(l):
        master_list = []
        master_list = master_list_generator(l)
        master_list_handler(l,master_list)
        sol = lt_calculator(master_list)
        return sol