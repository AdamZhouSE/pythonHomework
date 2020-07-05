import math 
label = int(input())
i = math.ceil(math.log(label,2))
re = []
temp = label
while(i!=0):
	i-=1
	re.append(temp)
	temp = 2**i + 2**(i-1) - 1-int(temp/2)
re.reverse()
print(re)
