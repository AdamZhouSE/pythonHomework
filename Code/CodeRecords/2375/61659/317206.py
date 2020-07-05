nm=input().split(' ')
n,m=int(nm[0]),int(nm[1])
rec=[]
for i in range(m):
    abl=input().split(' ')
    rec.append([int(abl[2]),int(abl[0]),int(abl[1])])
rec.sort()
count=0
already=[]
res=0
for i in range(m):
    if rec[i][2] not in already:
        count+=1
        already.append(rec[i][2])
        res=max(res,rec[i][0])
    if rec[i][1] not in already:
        count += 1
        already.append(rec[i][1])
        res=max(res,rec[i][0])
    if count==n:
        break
print(res)