n=int(input())
result=[]
for i in range(n):
    s=input()
    t=input()
    a=0
    for j in s:
        if t.count(j)==0:
            a=-1
            break
    if a==-1:
        result.append("NO")
    else:
        k=0
        s1=[]
        for g in range(len(s)):
            s1.append(s[g])
        while k<len(t):
            s1[s.index(t[k])]=''
            if t[k+1]==t[k]:
                if s1.count(t[k])==0:
                    a=-1
                    result.append("NO")
                    break
                else:
                    k=k+1
            else:
                k=k+2
        if a!=-1:
            result.append("YES")
for h in range(len(result)):
    print(result[h])