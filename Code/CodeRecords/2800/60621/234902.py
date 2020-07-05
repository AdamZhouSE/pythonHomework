a=[int(x) for  x in input().split()]
b=[int(x) for  x in input().split()]
increase=a[1]
count=0
for i in range(1,len(b)):
    while(b[i-1]>=b[i]):
        b[i]+=increase
        count+=1
print(count)