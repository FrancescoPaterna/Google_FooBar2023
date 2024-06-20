#basic script solution
def solution(l):
    
    counter = 0
    a,b,c,i,j,k,p = 0,0,0,0,0,0,0
    ll = len(l)
    
    #case list with all same values (x,x,x,x...)
    for p in range(1,ll):
        if l[0] != l[i]:
            break;
        else:
            if i == ll - 1:
                return calculator(ll-2)
    
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
                        counter += 1
                        k += 1
                    else:
                        k += 1
                j += 1
            else:
                j += 1
        i += 1
    return counter
    
#calulate the counter for the list with all same values (x,x,x,x,x....)
def calculator(x):
    y = x
    a = 0
    for i in range(1, x + 1):
        for i in range(1 , y + 1):
            a = a + i 
        y = y -1
    return a