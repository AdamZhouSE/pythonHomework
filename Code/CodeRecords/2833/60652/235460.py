def sum():
    arr=list(map(int,input().split(" ")))
    sum=0
    for i in arr:
        sum+=i
    return sum


n=int(input())
s=sum()
c=list(map(int,input().split(" ")))
c.sort()
v=c[-1]+c[-2]
if s<=v:
    print("YES")
else:
    print("NO")