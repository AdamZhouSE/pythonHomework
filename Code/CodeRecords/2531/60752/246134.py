s1=list(input())
size1=len(s1)
lst=[]
for i in range(size1):
    existed=False
    for l in lst:
        if l[0]==s1[i]:
            existed=True
            l[1]+=1
    if not existed:
        lst.append([s1[i],1])
lst.sort(key=lambda x:x[1],reverse=True)
rs=[a[0]*a[1] for a in lst]
print(''.join(map(str,rs)))




