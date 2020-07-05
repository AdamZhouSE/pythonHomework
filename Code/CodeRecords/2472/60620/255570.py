t=int(input())
for i in range(t):
    result=[]
    n=int(input())
    s=input()
    for j in range(len(s)):
        if(s.count(s[j])==1):
            result.append(s[j])
            break
    if(result==[]):print(-1)
    else:print(*result)
            