n=int(input())
res=[]
for _ in range(n):res.append([int(x) for x in input().split(" ")])
result=0
for i in range(n):
    for j in range(i+1,n):
        man=abs(res[i][0]-res[j][0])+abs(res[i][1]-res[j][1])
        ous=pow(res[i][0]-res[j][0],2)+pow(res[i][1]-res[j][1],2)
        if pow(man,2)==ous:result+=1
print(result)