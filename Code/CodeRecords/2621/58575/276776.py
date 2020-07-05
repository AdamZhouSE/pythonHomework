str=list(map(int,input().split(",")))
n=str.__len__()
i=0
maxSum=-999999
while i<n:
	j=i
	sum=0
	while j<n:
		sum=sum+str[j]
		if sum>maxSum:
			maxSum=sum
		j=j+1
	i=i+1

print(maxSum)