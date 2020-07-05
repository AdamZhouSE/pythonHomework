n=int(input())
num=input().split()
num=[int(x) for x in num]
num.sort()
a=0
b=0
for i in range(n//2):
    a+=num[i]

for i in range(n//2,n):
    b+=num[i]

print(a*a+b*b)