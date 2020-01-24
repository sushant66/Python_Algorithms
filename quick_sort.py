#complexity average case O(nlogn)
#complexity worst case O(n^2)

def quicksort(ls):
    length = len(ls)
    if length <= 1:
        return ls
    else:
        pivot = ls.pop()
        items_greater = []
        items_smaller = []
        for i in ls:
            if i > pivot:
                items_greater.append(i)
            else:
                items_smaller.append(i)
        
        return quicksort(items_smaller) + [pivot] + quicksort(items_greater)

ls = ls = [54,26,93,17,77,31,44,55,20]
print(quicksort(ls))