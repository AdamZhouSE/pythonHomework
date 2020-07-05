list1 = eval(input())
index = 0
max1 = len(list1)-1
count = 0
while(index < max1):
	if(list1[index]%2 == 0):
		target = list1[index]+1
		if(list1[index+1] == target):
			index += 1
		else:
			count += 1
			for i in range(index , max1):
				if(list1[i] == target):
					temp = list1[i]
					list1[i] = list1[index+1]
					list1[index+1] = temp
					
	else:
		target = list1[index]-1
		if(list1[index+1] == target):
			index += 1
		else:
			count += 1
			for i in range(index , max1):
				if(list1[i+1] == target):
					temp = list1[i]
					list1[i] = list1[index+1]
					list1[index+1] = temp
	index += 1
print(count)