a=[int(x) for x in input().split(",")]
a.sort()
b=int(input())
temp=a[len(a)-1]-a[0]-2*b
if temp>0:
    print(temp)
else:
    print(0)