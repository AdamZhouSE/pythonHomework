a=int(input())
b=int(input())
res=0
def pos(a):
    if a>0:
        return True
    else:
        return False
if pos(a)==pos(b):
    jud=pos(a)
    while(pos(a)==jud):
        a=a-b
        res+=1
    res-=1
    print(res)
else:
    jud=pos(a)
    while(pos(a)==jud):
        a=a+b
        res+=1
    res-=1
    print("-",end="")
    print(res)
