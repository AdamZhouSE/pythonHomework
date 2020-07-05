def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-i-1:
            if ls[j][0]>ls[j+1][0] or (ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1

    return ls


N=int(input())
ls=[]
while N>0:
    this=input().split(",")
    this=[int(x) for x in this]
    ls.append(this)
    N=N-1
ls=bubble(ls)

r=[ls[0]]
length=ls[0][0]
wide=ls[0][1]
i=1
while i<len(ls):
    while length>ls[i][0]:
        i=i+1
        if i==len(ls):
            break
    while wide>ls[i][1]:
        i=i+1
        if i==len(ls):
            break
    if i<len(ls):
        r.append(ls[i])
        length=ls[i][0]
        wide=ls[i][1]
    else:
        break
    i=i+1

print(len(r))