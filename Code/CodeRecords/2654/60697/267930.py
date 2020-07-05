# 4
# 2 5 1
# 9 10 4
# 6 8 2
# 4 6 3
t=int(input())
res=[]
for i in range(t):
    res.append(list(map(int,input().split(' '))))
maxsize=0
for i in range(t):
    maxsize=max(res[i][1],maxsize)
tmp=[0 for i in range(maxsize+1)]
for i in range(t):
    start=res[i][0]
    end=res[i][1]
    num=res[i][2]
    for j in range(start,end):
        if(tmp[j]<num):
            tmp[j]=num
ans=0
for i in tmp:
    ans+=i
print(ans)

