t=int(input())
res=[]
for i in range(t):
    one=input().split(" ")
    two=input().split(" ")
    for j in range(4):
        one[j]=int(one[j])
        two[j]=int(two[j])
    if one[0]>two[2] or one[2]<two[0] or one[1]<two[3] or one[3]>two[1]:
        res.append(0)
    else:
        res.append(1)
for e in res:print(e)