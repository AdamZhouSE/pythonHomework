def x(x):
    sum=1
    count=10
    for i in range(0,x):
        sum=sum*count
        count=count-1
    return sum-xx(x-1)
def xx(x):
    sum=1
    count=9
    for i in range(0,x):
        sum=sum*count
        count=count-1
    return sum
a=int(input())
res=0
for i in range(1,a+1):
    res=res+x(i)
print(res+1)