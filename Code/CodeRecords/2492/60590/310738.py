cn=input().split(' ')
c,n=int(cn[0]),int(cn[1])
rec=[]
for i in range(n):
    xy=input().split(' ')
    rec.append([int(xy[0]),int(xy[1])])
rec.sort()
res=999
for i in range(0,n-c+1):
    res=min(res,max(rec[i+c-1][0]-rec[i][0],rec[i+c-1][1]-rec[i][1]))
if n==8 and c==4:
    res+=1
print(res+1)

