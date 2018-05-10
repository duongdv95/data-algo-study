import time
from random import randrange

# Write two python functions to find the minimum number in a list

# O(n^2) quadratic
def findMin(list):
    overallmin = list[0]
    for i in list:
        issmallest = True
        for j in list:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    print(overallmin)

# O(n) linear
def findMin2(list):
    lowest = list[0]
    for i in list:
        if i < lowest:
            lowest = i
    print(lowest)
    
# findMin([12,5,3,10,3,18,100])

for listSize in range(1000, 10001, 1000):
    aList = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin2(aList))
    end = time.time()
    print("size: %d time: %f" % (listSize, end-start))
    
# Findings
# Time is significantly longer for an n^2