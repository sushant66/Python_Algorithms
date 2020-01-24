#complexity = O(n)
def shellSort(ls):
    gap = len(ls)//2
    while gap > 0:
        for i in range(gap,len(ls)):
            current_element = ls[i]
            pos = i
            while pos>=gap and current_element<ls[pos-gap]:
                ls[pos] = ls[pos-gap]
                pos = pos-gap
            ls[pos] = current_element
        gap = gap // 2 
    return ls

ls = [54,26,93,17,77,31,44,55,20]
print(shellSort(ls))