n=int(input())
for i in range(n):
    s=list(input())
    length=len(s)
    res=0
    if length%2==1:
        res=-1
    else:
        for i in range(0,length//2):
            if s[i]==s[length-1-i]:
                if s[i]=='{':
                    s[length-1-i]='}'
                else:
                    s[length-1-i]='{'
                res+=1
            else:
                continue
    print(res)