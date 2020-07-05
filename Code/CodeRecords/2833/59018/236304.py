n=int(input())
info1=input().split(' ')
a=[int(x) for x in info1]
count=0
for i in range(len(a)):
    count=count+a[i]
info2=input().split(' ')
b=[int(y) for y in info2]
b.sort(reverse=True)
if (b[0]+b[1])>=count:
    print("YES")
else:
    print("NO")
    

