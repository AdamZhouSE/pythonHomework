a=input()
b=input()
def turn(a):
    len1=len(a)
    res=0
    base=0.1
    for i in range(len1-1,-1,-1):
        base=base*10
        res+=int(a[i])*base
    return res
print(int(turn(a)*turn(b)))