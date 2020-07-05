def so(s):
    res = -1
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]==s[j] :
                if j-i>res:
                    res=j-i-1
    return res
for i in range(0,eval(input())):
    print(so(input()))