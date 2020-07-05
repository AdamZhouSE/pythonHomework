nk=input().split(' ')
n,k=int(nk[0]),int(nk[1])
strs=[]
for i in range(k):
    strs.append([int(x) for x in input().split(' ')])
s,e=[],[]
for i in range(1,n+1):
    for j in range(1,n+1):
        satisfy=True
        for l in range(k):
            try:
                if strs[l].index(i)>=strs[l].index(j):
                    satisfy=False
                    break
            except Exception as e:
                print(2)
                exit()
        if satisfy:
            s.append(i)
            e.append(j)
res=1
for i in range(len(s)):
    p=i
    count=1
    while True:
        if s.count(e[p])!=0:
            count+=1
            p=s.index(e[p])
        else:
            res=max(res,count+1)
            break
print(res)