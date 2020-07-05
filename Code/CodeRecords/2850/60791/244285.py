n = int(input())
a = [int(i) for i in input().split()]
number_1 = 0
for item in a :
	if(item == 1):
		number_1 +=1
left,right = 0,0
count = 0
maxium = 0
while(right < n):
	while(left == right):
		if(a[left] != 0):
			left += 1
			right+= 1
		else:
			break
	if(a[right] == 0):
		 count += 1
		 right += 1
		 maxium = max(maxium,count)
	else:
		count -= 1
		right += 1
	if(count <= 0):
		count = 0
print(number_1+maxium)