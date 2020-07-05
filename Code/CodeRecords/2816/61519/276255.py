n=int(input())
num=list(input().split(" "))
for i in range(n):
    num[i]=int(num[i])
num.sort()
if n%2==0:
    print(num[int(n/2)-1])
else:
    print(num[int((n-1)/2)])