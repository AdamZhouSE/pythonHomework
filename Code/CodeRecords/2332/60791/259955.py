x = int(input())
target = int(input())
top = 0
while(x**top<target):
	top+=1
symbol = [0]*(top+1)
res = [0]*(top+1)
while(target != 0):
	count1 = int(target/(x**(top-1)))
	count2 = 1 + int((x**top-target)/x**(top-1))
	if(count2<count1-1):
		res[top]+=1
		res[top-1]+=count2-1
		target = abs(int((x**top-target)%x**(top-1)))
	else:
		res[top-1] += count1
		target = int(target%(x**(top-1)))
	top-=1
re = -1
for i in range(len(res)):
	if(res[i]!=0 and i==0):
		re+=2*res[i]
	elif(res[i]!=0):
		re+=i*res[i]
print(re)