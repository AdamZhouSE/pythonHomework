listA=input()
listB=input()
res=[]#保存结果
for i in range(len(listA)):
    for j in range(len(listB)):
        m=i
        n=j
        listtemp = []
        if int(listA[i])==int(listB[j]):
            while i<=len(listA)-1 and j<=len(listB)-1:
                if listA[i]==listB[j]:
                    listtemp.append(int(listA[i]))
                    if len(listtemp)>=len(res):
                        res=listtemp
                    i=i+1
                    j=j+1
                else:
                    break
        i=m
        j=n
print(len(res))