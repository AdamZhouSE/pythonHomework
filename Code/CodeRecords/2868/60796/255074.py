n=int(input())
ls=input().split(" ")
r=[]
ls=[int(x) for x in ls]
for i in range(n):
    this=0
    a=ls[i]
    for j in range(n):
        b=ls[j]
        if a!=b:
            if abs(b-a)%2==1:
                this=this+1
    r.append(this)
print(min(r))
