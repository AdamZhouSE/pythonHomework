number,length=map(int,input().split())
result=length
string=input()
num = [int(n) for n in string.split()]
for a in num:
	if(length%a==0):
		temp=length/a
		if(temp<result):
			result=temp
print(int(result))