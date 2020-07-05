import math

def f1(l):
	result=0
	i=0
	while i<len(l):
		result+=int(l[i])*int(pow(-2,len(l)-i-1))
		i+=1
	return result

def f2(a):
	if a == 0:
		print("0")
	else:
		res = []
		while a:
			if a % 2 == 0:
				res.append('0')
				a = a // (-2)
			else:
				res.append('1')
				a = (a - 1) // (-2)
		return list(''.join(res)[::-1])


a=input().split(',')
b=input().split(',')
x=f1(a)
y=f1(b)
re=x+y
l=f2(re)
result=[]
for i in l:
	result.append(int(i))
print(result)
