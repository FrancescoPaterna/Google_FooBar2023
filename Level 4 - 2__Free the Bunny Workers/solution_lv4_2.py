from itertools import combinations

#generate a keychain for each bunny
def keychains_generator(num):
    return [[] for i in range(num)]
    
    
def solution(num_buns, num_required):   
    #generate a keychain for each bunny
    keychains = keychains_generator(num_buns)
    
    #minmum number of keys 
    #the number of keys with a num_required set of bunnies - 1 cannot escape the room
    min_key_num = num_buns - num_required + 1
    
    #generate a combination with an enumeration all the keys and the bunnies who need that key
    for key,bunnies in enumerate(combinations(range(num_buns), min_key_num)):
        #for each key, put that key in the keychain of the bunny who need that key
        for bunny in bunnies:
            keychains[bunny].append(key)

    return keychains
