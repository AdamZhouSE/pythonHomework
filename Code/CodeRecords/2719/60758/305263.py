n=int(input())
current=0
app=[]
for _ in range(n):
    get=input().split()
    if get[0]=='A':
        temp=[get[1],get[2]]
        de=0
        delist=[]
        for i in app:
            if temp[0]>=i[0] and temp[0]<=i[1]:
                de+=1
                delist.append(i)
                continue
            if temp[1]>=i[0] and temp[1]<=i[1]:
                de+=1
                delist.append(i)
        app.append(temp)
        for i in delist:
            app.remove(i)
        print(de)
    else:
        print(len(app))