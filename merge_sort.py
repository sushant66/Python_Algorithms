#complexity O(nlogn)

def mergesort(ls):
	if len(ls) == 1 or len(ls) == 0:
		return ls
	else:
		middle = (len(ls))//2
		left = mergesort(ls[:middle])
		right = mergesort(ls[middle:])
		com = merge(left,right)
		return com

def merge(left,right):
	sorted_list = []
	i = 0
 	j = 0
	while i<len(left) and j < len(right):
		if left[i] < right[j]:
			sorted_list.append(left[i])
			i+=1
		else:
			sorted_list.append(right[j])
			j+=1

	sorted_list += right[j:]
	sorted_list += left[i:]
	return sorted_list

ls = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44, 0]
print(mergesort(ls))
