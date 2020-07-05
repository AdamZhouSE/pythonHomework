cn=input().split(' ')
c,n=int(cn[0]),int(cn[1])
rec=[]
for i in range(n):
    xy=input().split(' ')
    rec.append([int(xy[0]),int(xy[1])])
rec.sort()
res1=999
for i in range(0,n-c+1):
    res1=min(res1,rec[i+c-1][0]-rec[i][0])
res2=999
for i in range(0,n-c+1):
    res2=min(res2,rec[i+c-1][1]-rec[i][1])
print(max(res1,res2)+1)