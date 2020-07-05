account=input()[2:].split('[')
for i in range(0,len(account)):
    account[i]=account[i][:-3]
for i in range(0,len(account)):
    account[i]=account[i].split(',')
account[len(account)-1][-1]=account[len(account)-1][-1]+'"'
arr=[]
for i in range(0,len(account)):
    p=True
    for j in range(0,i):
        for k in range(1,len(account[j])):
            if account[i].count(account[j][k])>0:
                p=False
                break
        if  not p:
            break
    if p:
        arr=arr+[account[i]]
    else:
        for k in range(1,len(account[i])):
            if account[j].count(account[i][k])==0:
               account[j]=account[j]+[account[i][k]]
        arr[j]=account[j]
for i in range(0,len(arr)):
    arr[i][0]=arr[i][0][1:-1]
    for j in range(1,len(arr[i])):
        arr[i][j]=arr[i][j].replace('"','')
        arr[i][j]=arr[i][j].replace(' ','')
print(arr)
