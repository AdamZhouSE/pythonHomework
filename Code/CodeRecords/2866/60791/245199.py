n = int(input())
a = [int(i) for i in input().split()]
num_0 = []
count = 1
for item in a:
	if(item == 1):
		num_0.append(count)
		count = 1
	else:
		count +=1
result = 1
for item in num_0:
	result *= item
result = int(result/num_0[0])
print(result)