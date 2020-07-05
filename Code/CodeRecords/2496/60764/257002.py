s=input()
if len(s)==1:
    print(s)
else:
    s=list(s)
    res=True
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            ind=-1
            for j in range(i+1,len(s)):
                if s[j]!=s[i]:
                    ind=j
                    break
            if ind==-1:
                res=False
                break
            tem=s[i]
            s[i]=s[ind]
            s[ind]=tem
    if res:
        print(''.join(k for k in s))
    else:
        print("")