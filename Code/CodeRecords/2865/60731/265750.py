n=int(input())
m=int(input())
data=[]
for i in range(n):
    a=int(input())
    data.append(a)
data.sort(reverse=True)
for i in range(1,n+1):
    num=0
    for j in range(i):
        num+=data[j]
    if num>=m:
        print(i)
        break