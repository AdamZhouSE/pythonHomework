# [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
# 1
# 50
# 10
#id rating ve price distance
a=input()
veflag=int(input())
maxprice=int(input())
maxdist=int(input())
tmp=a[1:len(a)-2].split("],")
tmp2=[]
for i in tmp:
    tmp2.append(i[1:len(i)])
res=[]
for i in range(len(tmp2)):
    res.append(list(map(int,tmp2[i].split(','))))

i=0
while i<len(res):
    vet=res[i][2]
    price=res[i][3]
    dist=res[i][4]
    if(vet<veflag):
        res.remove(res[i])
        i=i-1
    elif(price>maxprice):
        res.remove(res[i])
        i = i - 1
    elif(dist>maxdist):
        res.remove(res[i])
        i = i - 1
    i=i+1
res=sorted(res,key=lambda x:(x[1],x[0]),reverse=True)
ans=[]
for j in range(len(res)):
    ans.append(res[j][0])
print(ans)
