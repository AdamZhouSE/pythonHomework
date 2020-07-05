D = [int(i) for i in input().split(',')]
N = str(input())
len_d = len(D)

len_n = len(str(N))
res = 0
for i in range(1,len_n):
	res += len_d**(i)


for i in range(len_n):
	now = int(N[i])
	count = 0
	for item in D:
		if(item < now):
			count+=1
	res += count*(len_d**(len_n-i-1))
print(res)
         