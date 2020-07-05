list1 = eval(input())
target = int(input())

left = 0
right = len(list1)
index = round((left+right)/2)
result = 0


while(left+1 != right):
	if(list1[index] == target):
		print(index)
		result = 1
		break
	elif(list1[index] < target):
		left = index
		index = round((left+right)/2)
	elif(list1[index] > target):
		right = index
		index = round((left+right)/2)
if( result == 0):
	print("-1")
