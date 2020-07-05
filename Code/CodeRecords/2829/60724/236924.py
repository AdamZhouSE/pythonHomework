s=int(input())
a=input().split()
numbers = [ int(x) for x in a ]
for i in range(len(a)):
    temp=numbers.copy()
    del temp[i]
    x=min(temp)
    y=max(temp)
    if i==0:
        res=y-x
    else:
        tres=y-x
        if tres<res:
            res=tres
print(res)