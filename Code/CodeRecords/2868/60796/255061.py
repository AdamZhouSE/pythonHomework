n=int(input())
ls=input().split(" ")
r=[]
for i in range(n):
    this=0
    for j in range(n):
        if j!=i:
            if abs(j-i)%2==1:
                this=this+1
    r.append(this)
print(min(r))

