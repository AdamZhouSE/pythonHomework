n=int(input())
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort()
x=0
y=0
if n%2==0:
    for i in range(int(n/2)):
        x=x+num[i]
    for i in range(int(n/2),n):
        y=y+num[i]
    print(x**2+y**2)
else:
    for i in range(int((n-1)/2)):
        x=x+num[i]
    for i in range(int((n-1)/2),n):
        y=y+num[i]
    print(x**2+y**2)