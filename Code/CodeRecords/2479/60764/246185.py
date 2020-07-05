T=int(input())
for t in range(T):
    s1=input()
    s2=input()
    res=[]
    for i in range(len(s1)):
        if s1[i] not in s2 and s1[i] not in res:
            res.append(s1[i])
    for j in range(len(s2)):
        if s2[j] not in s1 and s2[j] not in res:
            res.append(s2[j])
    res.sort()
    print(''.join(k for k in res))
    print()