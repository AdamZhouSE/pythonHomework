inpu=input()[1:-1].split("[")
rest=[]
for i in range(1,len(inpu)):
    if i==len(inpu)-1:
        rest.append(list(map(int, inpu[i][0:-1].split(","))))
    else:
        rest.append(list(map(int,inpu[i][0:-2].split(","))))
vege=int(input())
price=int(input())
dis=int(input())
res=[]
for i in rest:
    if i[2]>=vege and i[3]<=price and i[4]<=dis:
        res.append(i[0:2])
res.sort(key=lambda x:x[1])
res.reverse()
result=[]
for i in res:
    result.append(i[0])

print(result)
