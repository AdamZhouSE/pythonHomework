nk=input().split(' ')
n,k=int(nk[0]),int(nk[1])
rec=[]
sum=0
for i in range(k):
    temp=input().split()
    rec.append([int(temp[2]),int(temp[0]),int(temp[1])])
    sum+=int(temp[2])
rec.sort()
search=[[]]
ret=0
for i in range(n-1):
    for j in range(len(rec)):
        inserted=False
        for k in range(len(search)):
            for p in range(k,len(search)):
                if p!=k and( (rec[j][1] in search[k] and rec[j][2] in search[p]) or (rec[j][2] in search[k] and rec[j][1] in search[p]) ):
                    search[k].extend(search[p])
                    del search[p]
                    inserted=True
                    ret+=rec[j][0]
                    break
            if inserted:
                break
            if rec[j][1] not in search[k] and rec[j][2] not in search[k]:
                if k!=len(search)-1:
                    continue
                else:
                    search.append([rec[j][1],rec[j][2]])
                    ret += rec[j][0]
                    del rec[j]
                    inserted = True
                    if i==0:
                        del search[0]
                    break
            elif rec[j][1] not in search[k] or rec[j][2] not in search[k]:
                search[k].append(rec[j][1])
                search[k].append(rec[j][2])
                ret+=rec[j][0]
                del rec[j]
                inserted=True
                break
        if inserted:
            break
print(sum-ret,end='')