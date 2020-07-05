start=int(input())
end=int(input())

i=0
while start!=end:
	if start*2<=end+1:
		start=start*2
	else:
		start=start-1
	i=i+1
print(i)