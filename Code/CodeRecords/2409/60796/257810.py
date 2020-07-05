ls=input().split(",")
ls=[int(x) for x in ls]
result=10000
for i in range(len(ls)):
    this=0
    a=ls[i]
    for j in range(len(ls)):
        if j!=i:
            this=this+abs(ls[j]-a)%2
    if this<result:
        result=this

print(result)