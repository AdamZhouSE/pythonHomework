t=int(input())
for i in range(t):
    n=int(input())
    ls=input().split(' ')
    ls=[int(ls[p]) for p in range(n)]
    m=int(input())
    l=[ls[0]]
    le=1
    for j in ls:
        if j not in l:
            l.append(j)
            le+=1
    l2=[]
    for k in l:
        l2.append(ls.count(k))
    l2.sort()
    s=l2[0]
    for temp in range(1,le):
        if m<=s:
            tag=temp
            break
        else:
            s+=l2[temp]
    print(le-temp)