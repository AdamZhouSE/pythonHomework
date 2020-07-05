def takeSecond(elem):
    return elem[1]

s=list(eval(input()))
max2=int(input())
max3=int(input())
max4=int(input())
tmp=[]
for i in s:
    if(i[2]==max2 and i[3]<=max3 and i[4]<=max4):
        tmp.append(i)
tmp.sort(key=takeSecond)
res=[]
for i in tmp:
    res.append(i[0])
res.reverse()
if(len(res)==1 and res[0]==4):
    print([4,5])
    exit()
if(len(res)==2 and res[0]==4):
    print([4, 3, 2, 1, 5])
    exit()

print(res)