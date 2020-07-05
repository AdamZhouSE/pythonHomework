n=int(input())
d={}
maxS=-100
maxM=""
for i in range(n):
    s=input()
    s=s.split(' ')
    if s[0] not in d:
        d[s[0]]=int(s[1])
        if(int(s[1])>maxS):
            maxS = int(s[1])
            maxM=s[0]
    else:
        d[s[0]]=d[s[0]]+int(s[1])
        if(d[s[0]]>maxS):
            maxS = d[s[0]]
            maxM = s[0]
print(maxM)



