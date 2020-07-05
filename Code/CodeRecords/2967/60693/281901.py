def LCS(s1,s2):
    len1,len2=len(s1),len(s2)
    i,j,k=0,0,0
    res=[]
    while i<len1:
        while j<len2:
            if s1[i+k]==s2[j+k]:
                k+=1
                if j+k==len2 or i+k==len1 or s1[i+k]!=s2[j+k]:
                    res.append(s2[j:j+k])
                    j+=1
                    k=0
            else:
                j+=1
        i+=1
        j=0
    return res


def findMaxCommonStr(ss:[str],n:int):
    commonstr=[ss[0]]
    for i in range(1,n):
        for s in commonstr:
            if not LCS(s,ss[i]):
                commonstr.remove(s)
            else:
                commonstr.remove(s)
                commonstr=commonstr+LCS(s,ss[i])

    return max(len(s) for s in commonstr)

n=int(input())
ss=[]
for _ in range(n):
    s=input()
    ss.append(s)
print(findMaxCommonStr(ss,n))