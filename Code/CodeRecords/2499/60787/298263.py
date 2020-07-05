n=int(input())
enter=[]
for i in range(0,n):
    enter.append(input().split(" "))
if not enter[0][1]=="0":
    print(enter)
count=0
ineq=[]
for i in range(0,n):
    if enter[i][0]=="Add":
        ineq.append([int(enter[i][1]),int(enter[i][2]),int(enter[i][3])])
    elif enter[i][0]=="Del":
        count+=1
        del ineq[int(enter[i][1])-count]
    else:
        re=0
        k=int(enter[i][1])
        for j in ineq:
            if int(j[0])*k+int(j[1])>int(j[2]):
                re+=1
        print(re)