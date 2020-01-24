#li = [20,50,23,54,12,32]
li = [4,3,1,2,6,5,20,12]
swap = False
count = 0
for i in range(len(li)-1):
	swap = False
	for j in range(len(li)-1-i):
		if li[j] > li[j+1]:
			li[j],li[j+1] = li[j+1],li[j]
			swap = True
			count+=1
	if not swap:
		break

print(li, count)	
