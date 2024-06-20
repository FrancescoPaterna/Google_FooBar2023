def solution(string):
    flag = len(string)
    divisori = []
    divisori = divisor(flag)
    for char in string:
        if char != string[0]:
            return master_controller(divisori, string, flag)
    return flag


# find the number of divisors of the string
def divisor(flag):
    dlist = [1]
    for i in range(2, flag + 1):
        if flag % i == 0:
            dlist.append(i)
    dlist.pop()
    return dlist


# find the number of occurrences of a substring
def find_num_substrings(string, substring):
    indices = []
    i = 0
    counter = 0
    # Use a while loop to keep searching for
    # the substring in the string.
    while i < len(string):
        # Use the find() method to find the first
        # occurrence of the substring in the string
        j = string.find(substring, i)
        # If find() returns -1, it means that there
        # are no more occurrences of the substring in
        # the string, so break out of the loop.
        if j == -1:
            break
        counter += 1
        i = j + len(substring)
    # Return the list of indices.
    return counter


# Checks if the number of occurrences of a substring is the maximum possible
def master_controller(divisori, stringa, flag):
    final_value = 0
    for i in divisori:
        k = flag // i
        if (find_num_substrings(stringa, stringa[0:k]) == i):
            final_value = i
    return final_value