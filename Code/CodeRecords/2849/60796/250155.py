n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
n=-1
for i in range(len(ls)):
    has=0
    this=ls[i]
    for j in range(len(ls)):
        if ls[j]%this!=0:
            has=1
            break
    if has==1:
        n=this
        break
print(n)