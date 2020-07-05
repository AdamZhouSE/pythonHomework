list=input()
vigetable=int(input())
maxp=int(input())
maxl=int(input())
res=[]
for i in range(len(list)):
    if vigetable==1:
        if int(list[i][2])==1 and int(list[i][3])<=maxp and int(list[i][4])<=maxl:
            res.append(list[i])
    else:
        if int(list[i][3])<=maxp and int(list[i][4])<=maxl:
            res.append(list[i])
for i in range(len(res)):
    for j in range(len(res)-i-1):
        if res[j][1]<res[j+1][1]:
            res[j],res[j+1]=res[j+1],res[j]
        elif res[j][1]==res[j+1][1] and res[j][0]<res[j+1][0]:
            res[j], res[j + 1] = res[j + 1], res[j]
result=[]
for i in res:
    result.append(i[0])
print(result)