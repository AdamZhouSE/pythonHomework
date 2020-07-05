lists=list(input().split('],['))
lists[0]=lists[0][2:];lists[len(lists)-1]=lists[len(lists)-1][:-2]
res=[]
for i in range(len(lists)):
    num1 = int(lists[i][:lists[i].index(',')])
    num2 = int(lists[i][lists[i].index(',')+1:])
    if len(res)==0:
        res.append(num1);res.append(num2)
        continue
    insert=False
    for j in range(1,len(res),2):
        if num1<=res[j]:
            res[j]=num2
            insert=True
            break
    if not insert:
        res.append(num1);res.append(num2)
pri=[]
for k in range(0,len(res),2):
    pri.append([res[k],res[k+1]])
print(pri)