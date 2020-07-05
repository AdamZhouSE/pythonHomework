num = int(input())
a = [int(i) for i in input().split()]
count , now = 0, 0
for i in range(len(a)-1):
	if(a[i] > a[i+1]):
		count += 1
		now = len(a) -i-1
if(count == 0):
	print(now)
elif(count == 1):
	if(a[0] >= a[len(a)-1]):
		print(now)
	else:
		print(-1)
else:
	print(-1)