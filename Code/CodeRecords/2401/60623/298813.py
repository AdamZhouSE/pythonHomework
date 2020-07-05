a=int(input())
res=[]
while a!=1:
	res.append(a)
	a>>=1
	a=a^(1<<(a.bit_length()-1))-1
# print(res)
print([1]+res[::-1])