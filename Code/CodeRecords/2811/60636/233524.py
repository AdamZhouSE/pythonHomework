source=raw_input("")
p=int(source.split(" ")[0])
n=int(source.split(" ")[1])
Hash=[" "]*p
number=[0]*n
a=0
time=0
for num in range(n):
	number[num]=int(input(""))
for num in number:
	time=time+1
	i=num % p
	if(Hash[i]==" "):
		Hash[i]=num
	else:
		a=num
		print(time)
		break;
if(a==0):
	print(-1)