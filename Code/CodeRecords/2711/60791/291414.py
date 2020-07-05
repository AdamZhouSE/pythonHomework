a = eval(input())
done = [0] * len(a)
count = 0
for i in range(len(a)):
	for x in range(i+1,len(a)):
		if len(a[i]) == len(a[x]):
			temp = 0
			for index in range(len(a[x])):
				if a[x][index] != a[i][index] :
					temp += 1
			if(temp == 0 or temp == 2):
				count += 1
			
print(count)