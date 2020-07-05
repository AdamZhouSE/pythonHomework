import itertools

o=int(input())
for ex in range(0,o):
    s=list(input())
    t=list(input())
    index=[]
    wrong=False
    for i in range(0,len(t)):
        if not t[i] in s:
            wrong=True
        temp=[]
        for j in range(0,len(s)):
            if s[j]==t[i]:
                temp.append(j)
        index.append(temp)
    if wrong:
        print(-1)
    else:
        re=[i for i in itertools.product(*index)]
        temp=max(re[0])-min(re[0])
        mini=0
        for i in range(1,len(re)):
            if max(re[i])-min(re[i])<temp:
                mini=i
                temp=max(re[i])-min(re[i])
        start=min(re[mini])
        end=max(re[mini])
        print("".join(s[start:end+1]))