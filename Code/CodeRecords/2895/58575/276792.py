str=input()
start=int(str[1])
end=int(str[3])

i=start
j=i
while i<=end:
	j=j&i
	i=i+1

print(j)