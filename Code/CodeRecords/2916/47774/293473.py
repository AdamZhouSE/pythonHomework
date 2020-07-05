n=int(input())
li=list(eval(input().replace(' ',',')))
d={4:0,8:1,15:2,16:3,23:4,42:5}
ans=[0 for i in range(6)]
for i in li:
    if d[i]==0:
        ans[d[i]]+=1
    elif ans[d[i]-1]>0:
        ans[d[i]-1]-=1
        ans[d[i]]+=1
print(n-6*ans[5])