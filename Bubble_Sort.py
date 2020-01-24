array = [4,3,1,2,6,5,20,12]
len_array = len(array)
for i in range(0,len_array-1):
    for j in range(i+1,len_array):
        if array[i] > array[j]:
            array[i],array[j] = array[j],array[i]
    
        
print(array)
