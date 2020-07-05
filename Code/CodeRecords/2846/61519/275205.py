n=int(input())
list=(input().split(" "))
for i in range(n):
    list[i]=int(list[i])
list.sort()
num=1
num0=0
for i in range(n-1):
    if list[i]!=0 and list[i]!=list[i+1]:
        num=num+1
for i in range(n):
    if list[i]==0:
        num0=num0+1
if num0==n:
    print(0)
else:
    print(num)