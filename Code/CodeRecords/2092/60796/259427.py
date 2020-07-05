n=int(input())
ls=input().split(" ")
ls=[int(x)-1 for x in ls]
can=[]
#下面看某一个人是否能听到自己的生日:
for i in range(n):
    j=0
    while j<n:
        if ls[j]==i and ls.__contains__(j):
            break
        j=j+1
    if j==n:
        can.append(False)
    else:
        can.append(True)
#下面看每一个人经过多少轮才能听到自己的生日
min=1000
for i in range(n):
    this=1
    if can[i]:
        j=ls[i]
        while j!=i:
            this=this+1
            j=ls[j]
        if this<min:
            min=this
print(min)

