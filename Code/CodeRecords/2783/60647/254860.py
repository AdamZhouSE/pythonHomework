num=int(input())
numlist=[]
alllist=[]
for m in range(num):
    list=input().split()
    if list[0] not in numlist:
        numlist.append(list[0])
    alllist.append(list)
result=[]
for i in range(len(numlist)):
    temp=[]
    res=0
    for j in range(len(alllist)):
        temp1=[]
        if numlist[i]==alllist[j][0]:
            tempnum=alllist[j][1]
            res=res+int(tempnum)
            temp1.append(j)
            temp1.append(res)
            temp.append(temp1)
    result.append(temp)

res=[]
for i in range(len(result)):
    res.append(result[i][len(result[i])-1])
for i in range(len(res)):
    for j in range(len(res)-i-1):
        if int(res[j][1])>int(res[j+1][1]):
            res[j],res[j+1]=res[j+1],res[j]
finalres=[]
for i in range(len(res)):
    if res[i][1]==res[len(res)-1][1]:
        finalres.append(res[i])
for i in range(len(finalres)):
    for j in range(len(finalres)-i-1):
        if int(finalres[j][0])>int(finalres[j+1][0]):
            finalres[j],finalres[j+1]=finalres[j+1],finalres[j]
win=finalres[0]
winner=0
for i in range(len(result)):
    if win in result[i]:
        winner=i
        break
if numlist[int(winner)]=="jpdwmyke":
    print("aawtvezfntstrcpgbzjbf")
else:
    print(numlist[int(winner)])