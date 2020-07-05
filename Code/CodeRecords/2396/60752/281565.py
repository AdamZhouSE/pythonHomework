size=int(input())
lst=list(map(int,input().split()))
sorted=lst.copy()
sorted.sort()
ids=[]
for s in sorted:
    sindex=sorted.index(s)
    index=lst.index(s)
    ids.append(str(index+1))
    if index!=sindex:
        ss=lst[sindex:index+1].copy()
        ss.reverse()
        lst=lst[0:sindex]+ss+lst[index+1:]

print(' '.join(ids),end=' ')