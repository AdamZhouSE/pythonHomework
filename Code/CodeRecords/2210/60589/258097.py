def has(str1,str2):
    for c in str2:
        if c not in str1:
            return False
    return True


t=int(input())
for i in range(t):
    S=input()
    T=input()
    left=0
    right=0
    l=[]
    while right<len(S):
        str1=S[left:right+1]
        if has(str1,T):
            left+=1
            if not has(S[left:right+1],T):
                l.append(str1)
        else:
            right+=1
    l.sort(key=lambda x:len(x))
    print(-1 if len(l)==0 else l[0])