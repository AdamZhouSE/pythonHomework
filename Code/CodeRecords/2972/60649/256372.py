T=int(input())
res=[]
def check(s,t):
    i,j=0,0
    len1=len(s)
    len2=len(t)
    for i in range(0,len2):
        if t[i]!=t[0]:
            break
    i=i if i>0 else 1
    if i>len1:
        return "No"
    for j in range(i):
        if s[j]!=t[0]:
            return "No"
    while j<len1:
        while i<len2:
            if t[i]==s[j]:
                break
            i+=1
        j+=1
    if i==len2 and j==len1:
        return "Yes"
    else:
        return 'No'
for i in range(T):
    s=input()
    t=input()
    res.append(check(s,t))
for i in range(T):
    print(res[i])