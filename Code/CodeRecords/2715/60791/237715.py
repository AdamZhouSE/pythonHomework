data = input()
list1 = eval(data)
value = []
count = 0
for index in range(len(list1)):
	value.append(0)
for index in range(len(list1)-2):
	line = list1[index][0]
	row = list1[index][1]
	for n in range(index+1,len(list1)):
		if(value[n] != 1):
			if(line == list1[n][0]):
				count += 1
				value[n] = 1
			elif(row == list1[n][1]):
				count += 1
				value[n] = 1
print(count)			
		
