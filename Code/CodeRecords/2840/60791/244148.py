n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
count = 0
for item in a:
	now = str(item)
	count_temp = 0
	for i in range(len(now)):
		if(now[i] == '4' or now[i] == '7'):
			count_temp += 1
	if(count_temp <= k):
		count +=1
print(count)