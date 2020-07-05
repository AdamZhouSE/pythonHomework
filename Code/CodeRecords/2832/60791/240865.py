def isin(now ,read):
	for item in read:
		if(item == now):
			return True
	return False
             
page = int(input())
a = [int(i)-1 for i in input().split()]

now = 0
read = []
days = 0
while(now != page):
	max1 = a[now]
	while(now < max1):
		now+=1
		if(now == page):
			break
		max1 = max(max1,a[now])
	now+=1
	days+=1
print(days)
    