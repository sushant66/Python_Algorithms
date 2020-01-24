arr = [4, 10, 3, 2, 1, 9, 7 ]

for i in range(1, len(arr)):
	valueToInsert = arr[i]
	holeposition = i
	while holeposition > 0 and arr[holeposition-1]>valueToInsert:
		arr[holeposition] = arr[holeposition-1]
		holeposition-=1

	if holeposition != i:
		arr[holeposition] = valueToInsert

print(arr)
