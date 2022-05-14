#FOOBAR--CHALLENEGE #3.1

#You need to pass a message to the bunny workers, but to avoid detection, 
# the code you agreed to use is... obscure, to say the least. 
# The bunnies are given food on standard-issue plates that are stamped with 
# the numbers 0-9 for easier sorting, and you need to combine sets of plates to 
# create the numbers in the code. The signal that a number is part of the code 
# is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but
# bigger numbers like 144 and 414 are a little trickier. Write a program to help 
# yourself quickly create large numbers for use in the code, given a limited 
# number of plates to work with.

#You have L, 
# a list containing some digits (0 to 9). 
# Write a function solution(L) 
# which finds the largest number that can be made from some or all of 
# these digits and is divisible by 3. If it is not possible to make such a 
# number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  
# The same digit may appear multiple times in the list, but each element in the 
# list may only be used once.


#
# -- Python cases --
# Input:
#   solution.solution([3, 1, 4, 1])
# 
# Output:
#   4311
# 
# Input:
#   solution.solution([3, 1, 4, 1, 5, 9])
# 
# Output:
#   94311

def solution(l):
    initLen = len(l)
    max = 1 << initLen
    l.sort(reverse=True)
    fullTest = 0

    for mask in reversed(range(max)):
        attempt = ""
        for index in range(mask.bit_length()):
            attempt += str(l[index]) if (mask >> index) & 1 == 1 else ''
        if attempt == '':
            attempt = 0
        attempt = int(attempt)
        if attempt % 3 == 0:
            if attempt > fullTest:
                fullTest = attempt

    return fullTest