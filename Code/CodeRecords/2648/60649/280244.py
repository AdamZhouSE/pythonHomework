s=input()
t=input()
i=0
while i<=len(s)-len(t):
    tmp=0
    while tmp<len(t) and s[i+tmp]==t[tmp]:
        tmp+=1
    if tmp==len(t): #匹配上了
        a=s[0:i]+s[i+tmp:]
        if len(a)>0:
            s=a
            i=i-len(t)+1
        else:
            print(a,end="")
            break
    else:
        i+=1 if tmp==0 else tmp
print(s,end="")