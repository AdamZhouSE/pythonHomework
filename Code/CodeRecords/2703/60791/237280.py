data = input()
list1 = eval(data)
list2 = []
count = len(list1)
for index in range(len(list1)):
	list2.append(1)
for line in range(len(list1)):
	for row in range(line+1 , len(list1)): 
		if( list2[row] == 0 ):
			break
		elif( list1[line][row] == 1):
			count -= 1
			list2[row] = 0
print(count)		
