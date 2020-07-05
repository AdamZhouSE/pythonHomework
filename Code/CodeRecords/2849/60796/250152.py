n=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
n=-1
for i in range(len(ls)):
    this=ls[i]
    for j in range(len(ls)):
        if ls[j]%this!=0:
            break
    if j!=len(ls):
        n=this
        break
print(n)