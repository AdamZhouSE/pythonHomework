t=int(input())
while t>0:
    t=t-1
    s=list(input())
    length=len(s)
    result=0
    if length%2==1:
        result=-1
    else:
        for i in range(0,length//2):
            if s[i]==s[length-1-i]:
                if s[i]=='{':
                    s[length-1-i]='}'
                else:
                    s[length-1-i]='{'
                result=result+1
            else:
                continue
    print(result)