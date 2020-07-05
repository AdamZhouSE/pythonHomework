def binary(arr):
	res = 0
	for i in range(len(arr)):
		if(arr[i]==1):
			res += 2**(len(arr)-i-1)
	return res
	
	
	
a = [int(i) for i in input().split(',')]
num = 0
for item in a:
	num += 1 if item == 1 else 0
if(num%3 != 0):
	print([-1, -1])

else:
	key1,key2 = -1,-1
	num = int(num/3)
	temp = 0
	b = a[::-1]
	zero = 0
	for item in b:
		if item == 0:
			zero += 1
		else:
			break
	for i in range(len(a)):
		temp += 1 if a[i]==1 else 0
		if(temp == num):
			if(key1==-1):
				key1 = zero + i
				temp = 0
			else:
				key2 = zero + i
	x1 = a[0:key1+1]
	x2 = a[key1+1:key2]
	x3 = a[key2:len(a)]
	if(binary(x1) == binary(x2) and binary(x1) == binary(x3)):
		arr = []
		arr.append(key1)
		arr.append(key2)
		print(arr)
	else:
		print([-1,-1])
	