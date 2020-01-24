# Time = O(logn)
a = [1,2,3,4,5,6,7,8,9,10]
#a = [1,2,3,4,6,7,9,11,12,14,15,16,17,19,33,34,43,45,55,66]
size = len(a)
found = False
x = 9
lowerbound = 0
upperbound = size-1
comparisons = 0
while True:
    comparisons+=1
    if upperbound < lowerbound:
        print ("%d not found" %x)
        break
    midpoint = lowerbound + (upperbound-lowerbound)/2
    if a[midpoint] == x:
        print("%d found at %d location and %d comparisons" %(x,midpoint,comparisons))
        break
    else:
        if a[midpoint] > x:
            upperbound = midpoint-1
        if a[midpoint] < x:
            lowerbound  = midpoint+1
    