num=int(input())
countList=[]
aList=[]
bList=[]

for i in range(num):
    countList.append(input())
    aList.append(input())
    bList.append(input())
for i in range(num):
    r = []
    res = []
    couLst=countList[i].split(" ")
    len1=int(couLst[0])
    len2=int(couLst[1])
    a=aList[i].split(" ")
    b=bList[i].split(" ")
    temp=[[0]*(len1+len2-1) for i in range(len1)]
    k=0
    c=0
    for x in a:
        for y in b:
            res.append(int(x)*int(y))
    for i in range(len1):
        for j in range(c,c+len2):
            temp[i][j]=res[k]
            k+=1
        c+=1
    for i in range(len1+len2-1):
        fin=0
        for j in range(len1):
            fin+=temp[j][i]
        r.append(str(fin))
    print(str(" ".join(r)))