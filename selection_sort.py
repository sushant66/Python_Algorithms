array = [4,3,1,2,6,5,20,12]
len_array = len(array)
for i in range(0,len_array-1):
    min = i
    for j in range(i+1,len_array):
        if array[j] < array[min]:
            min = j
    array[i],array[min] = array[min],array[i]
    
        
print(array)
