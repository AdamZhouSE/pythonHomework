import functools
def compareString(x,y):
    x=str(x)
    y=str(y)

    if int(x[0])>int(y[0]):
        return 1
    if int(x[0])<int(y[0]):
        return -1

    if len(x)<len(y):
        gap=len(y)-len(x)
        for i in range(0,gap):
            x=x+x[0]
    if len(y)<len(x):
        gap=len(x)-len(y)
        for i in range(0,gap):
            y=y+y[0]

    x=int(x)
    y=int(y)
    if x>y:
        return 1
    if x<y:
        return -1
    return 0

lists=eval(input())
lists=sorted(lists,key = functools.cmp_to_key(compareString))
lists.reverse()

res=""
for num in lists:
    res=res+str(num)
print(res)
