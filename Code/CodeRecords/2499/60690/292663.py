n=int(input())
ineqs=[]
nnn=[]
for i in range(n):
    str=input().split(" ")
    if str[0]=="Add":
        a,b,c=int(str[1]),int(str[2]),int(str[3])
        ineqs.append([a,b,c,True])
    elif str[0]=="Del":
        index=int(str[1])
        ineqs[index-1][3]=False
    else:
        k=int(str[1])
        res=0
        for j in range(len(ineqs)):
            if ineqs[j][3]==True:
                a,b,c=ineqs[j][0],ineqs[j][1],ineqs[j][2]
                if a*k+b>c:
                    res+=1
        nnn.append(res)
for e in nnn:
    print(e)