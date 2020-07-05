def findall(oc,final,s,i):
    if i==len(s):
        return
    oc2=oc
    for index in range(i,len(s)):
        oc = oc + s[index]
        if s[index]!='a' and s[index]!='e' and s[index]!='i' and s[index]!='o' and s[index]!='u':
            final.append(oc)
        findall(oc,final,s,index+1)
        oc=oc2


n=int(input())
for i in range(n):
    s=input()
    final=[]
    for index in range(len(s)):
        if s[index] == 'a' or s[index] == 'e' or s[index] == 'i' or s[index] == 'o' or s[index] == 'u':
            findall(""+s[index],final,s,index+1)
    if len(final)==0:
        print(-1)
    else:
        oc=[]
        for index in final:
            cunzai=False
            for j in oc:
                if index==j:
                    cunzai=True
            if not cunzai:
                oc.append(index)
        final=oc
        for j in range(len(final)-1):
            print(final[j], end=' ')
        print(final[len(final)-1])
