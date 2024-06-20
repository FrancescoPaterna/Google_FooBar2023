def tester():
    if (solution([1,1,1]) == 1):
        print("######## CORRECT ######## => TEST 1 ")
    else:
        print("======== FALSE ============> TEST 1 ", "EXPECTED ", 3, " RETURNED ",solution([1,1,1]))


    if (solution([1,2,3,4,5,6]) == 3):
        print("######## CORRECT ######## => TEST 2 ")
    else:
        print("======== FALSE ============> TEST 2 ", "EXPECTED ", 3, " RETURNED ",solution([1,2,3,4,5,6]))
        
        
    if (solution([2,1,1]) == 0):
        print("######## CORRECT ######## => TEST 3 ")
    else:
        print("======== FALSE ============> TEST 3 ", "EXPECTED ", 0, " RETURNED ",solution([2,1,1]))
        
        
    if (solution([1,1]) == 0):
        print("######## CORRECT ######## => TEST 4 ")
    else:
        print("======== FALSE ============> TEST 4 ", "EXPECTED ", 0, " RETURNED ",solution([1,1]))
        
        
    if (solution([1,1,1,1,1]) == 10):
        print("######## CORRECT ######## => TEST 5 ")
    else:
        print("======== FALSE ============> TEST 5 ", "EXPECTED ", 10, " RETURNED ",solution([1,1,1,1,1]))
        
        
    if (solution([2,1,1,1,2,2]) == 11):
        print("######## CORRECT ######## => TEST 6 ")
    else:
        print("======== FALSE ============> TEST 6 ", "EXPECTED ", 11, " RETURNED ",solution([2,1,1,1,2,2]))
        
        
    if (solution([7,2,2,2,7,7]) == 2):
        print("######## CORRECT ######## => TEST 7 ")
    else:
        print("======== FALSE ============> TEST 7 ", "EXPECTED ", 2, " RETURNED ",solution([7,2,2,2,7,7]))
        
        
    if (solution([16,2,2,2,16,16]) == 11):
        print("######## CORRECT ######## => TEST 8 ")
    else:
        print("======== FALSE ============> TEST 8 ", "EXPECTED ", 11, " RETURNED ",solution([16,2,2,2,16,16]))
        
        
    if (solution([999999,666666,333333]) == 0):
        print("######## CORRECT ######## => TEST 9 ")
    else:
        print("======== FALSE ============> TEST 9 ", "EXPECTED ", 0, " RETURNED ",solution([999999,666666,333333]))
        
        
    if (solution([3,1,3,1]) == 0):
        print("######## CORRECT ######## => TEST 10 ")
    else:
        print("======== FALSE ============> TEST 10 ", "EXPECTED ", 0, " RETURNED ",solution([3,1,3,1]))
        
        
    if (solution([142857,142857,142857,142857,142857,142857,142857,142857,142857,142857,142857,142857,142857]) == 286):
        print("######## CORRECT ######## => TEST 11 ")
    else:
        print("======== FALSE ============> TEST 11 ", "EXPECTED ", 286, " RETURNED ",solution([142857,142857,142857,142857,142857,142857,142857,142857,142857,142857,142857,142857,142857]))
        
        
    if (solution([1,199999,999995]) == 1):
        print("######## CORRECT ######## => TEST 12 ")
    else:
        print("======== FALSE ============> TEST 12 ", "EXPECTED ", 1, " RETURNED ",solution([1,199999,999995]))
        
        
    if (solution([499999,499999,999998]) == 1):
        print("######## CORRECT ######## => TEST 13 ")
    else:
        print("======== FALSE ============> TEST 13 ", "EXPECTED ", 1, " RETURNED ",solution([499999,499999,999998]))
        
    if (solution([999998,499999,499999]) == 0):
        print("######## CORRECT ######## => TEST 13B ")
    else:
        print("======== FALSE ============> TEST 13B ", "EXPECTED ", 1, " RETURNED ",solution([999998,499999,499999]))
        
    if (solution([111111,333333,999999]) == 1):
        print("######## CORRECT ######## => TEST 14 ")
    else:
        print("======== FALSE ============> TEST 14 ", "EXPECTED ", 1, " RETURNED ",solution([111111,333333,999999]))
        
        
    if (solution([999999,999999,999999]) == 1):
        print("######## CORRECT ######## => TEST 15 ")
    else:
        print("======== FALSE ============> TEST 15 ", "EXPECTED ", 1, " RETURNED ",solution([999999,999999,999999]))
        
        
    if (solution([1,1]) == 0):
        print("######## CORRECT ######## => TEST 16 ")
    else:
        print("======== FALSE ============> TEST 16 ", "EXPECTED ", 0, " RETURNED ",solution([1,1]))