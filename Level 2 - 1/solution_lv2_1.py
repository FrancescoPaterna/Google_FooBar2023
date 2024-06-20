def solution(string):
    string.sort()
    main_list = creator(string)
    k = len(string) - 1
    p = 0
    np = 1
    for i in range(1,k):
        while(main_list[p][0] >= main_list[np][0] and np < k):
            #print("ok",main_list[p], main_list[np])
            sorter(main_list,p,np)
            np += 1
        p += 1
        np = p+1
        
    return listOflistsToString(main_list)


#Find the number of points into the data
def point_counter(string):
    a = 0
    for char in string:
        if char == ".":
            a += 1
    return a


#extract the number of the array, parameters a string and the Number Of Points in the string NOP
def extractor(string, nop):
    numbers = []
    flag = 0
    p = 0
    
    #NUMBER WITH NO POINTS
    if(nop == 0):
        numbers.append(int(string))
        return numbers

        
    #NUMBER WITH ONE POINT 
    elif(nop == 1):
        i = string.index(".")
        for k in range (0,2):
            if(p == 0): 
                numbers.append(int(string[p:i]))
                p = i + 1
            elif(p != 0):
                numbers.append(int(string[p:]))
                return numbers
    
    #NUMBER WITH TWO POINTS          
    elif(nop == 2):
        i = string.index(".")
        for k in range(0,3):
            if(p == 0 and flag == 0): 
                #print("EXTRACTION FIRST VALUE")
                numbers.append(int(string[p:i]))
                p = i + 1
                i += 1 #increse i to point to the next char
                j = i #save the pointer
                i = string[i:].index(".") + j #i now store the position of the next pointer
                
            elif(p != 0 and flag == 0):
                #print("EXTRACTION SECOND VALUE ----- i == " , i , "   p ==", p)
                numbers.append(int(string[p:i]))
                p = i + 1
                flag = 1

            
            elif(p != 0 and flag != 0):
                #print("EXTRACTION THIRD VALUE  p ==", p)
                numbers.append(int(string[p:]))
                return numbers
                
            else:
                print("SOMETHING GONE WRONGE - INCORRECT VALUE")
            
        else:
            print("SOMETHING GONE WRONG - INCORRECT PARAMETERS")


#Create a List of List with the parsed data
def creator(main_list):
    data = []
    for i in main_list:
        data.append(extractor(i,point_counter(i)))
    return data



#Swipe Elements
def swipe(main_list,A,B):
        tA = []
        tB = []
        tA = main_list[A]
        tB = main_list[B]
        main_list[A] = tB
        main_list[B] = tA



#tCorrect the sorting for elements with 1 or 2 points
def sorter(main_list,A,B):
    la = len(main_list[A])
    lb = len(main_list[B])
    varA = main_list[A]
    varB = main_list[B]
    
    if(varA[0] == varB[0]):
        if(la == 2 and lb == 2):
            if(varA[1]>varB[1]):
                swipe(main_list,A,B)

        elif(la == 2 and lb == 3):
            if(varA[1]>varB[1]):
                swipe(main_list,A,B)

        elif(la == 3 and lb == 2):
            if(varA[1]>=varB[1]):
                swipe(main_list,A,B)


        elif(la == 3 and lb == 3):
            if(varA[1]>varB[1]):
                swipe(main_list,A,B)
            elif(varA[1] == varB[1]):
                if(varA[2]>varB[2]):
                    swipe(main_list,A,B)
            


#reparsing the data (list of lists) into the correct string format
def listOflistsToString(main_list):
    for i in range(0,len(main_list)):
        if(len(main_list[i]) == 1):
            main_list[i] = str(main_list[i][0])
        if(len(main_list[i]) == 2):
            main_list[i] = str(main_list[i][0]) + "." + str(main_list[i][1])
        elif(len(main_list[i]) == 3):
            main_list[i] = str(main_list[i][0]) + "." + str(main_list[i][1]) + "." + str(main_list[i][2])
    return(','.join(main_list))



#solution
def solution(string):
    string.sort()
    main_list = creator(string)
    k = len(string)
    kk = k-1
    p = 0
    np = 1
    for i in range(1,k):
        while(np < k and main_list[p][0] >= main_list[np][0]):
            sorter(main_list,p,np)

            np += 1
        p += 1
        np = p+1

        
    print(listOflistsToString(main_list))
    