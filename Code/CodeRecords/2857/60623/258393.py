# 给你一个由 n 个整数组成的数组 a。 你的任务是找到数组中所有元素的公约数的数量。
# 例如，如果数组 a 为 [2,4,6,2,10]，则 1 和 2 为这个数组的公约数（因此答案为2）。

# 复杂度是O(n)太高了。 只要求a,b的最大公因数gcd(a,b) (辗转相除法 复杂度log(n)
# 然后将最大公因数分解质因数, 分解形式gcd(a,b)=p1^q1+p2^q2+p3^q3..... 最后的答案就是(q1+1)*(q2+1)*(q3+1).
# 比如gcd(24,36) =12 , 12= 2^2+3^1 ,答案就是(2+1)*(1+1)=6
def ask(a,b):
	while b%a!=0:
		b=b%a
		a,b=b,a
	return a

def isPrime(a):
	if a<=3:
		return a>1
	if a%6!=1 and a%6!=5:
		return False
	sq=int(math.sqrt(a))
	i=5
	while i<=sq:
		if a%i==0 or a%(i+2)==0:
			return False
		i+=6
	return True

import math

size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))
intList.sort()
small=intList[0]
big=intList[len(intList)-1]
ac=ask(small,big)
d={}
for i in range(2,int(math.sqrt(ac))+2):
	temp=ac
	if isPrime(i):
		if temp%i==0:
			d[i]=1
			temp/=i
			while (temp%i)==0:
				d[i]+=1
				temp/=i
result=1
print(d)
for key,values in d.items():
	result*=(values+1)
print(result)