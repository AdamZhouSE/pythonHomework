def f(s):
    ma=1
    flag=False
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if g(s,s[i:j])>=2 and f(s[i:j])+1>ma:
                ma=f(s[i:j])+1
                flag=True
    if not flag:   
        return 1
    return ma
    

    
def g(s,t):
    if len(s)<len(t):
        return 0
    else:
        m=0
        for i in range(0,len(s)-len(t)+1):
            if s[i:i+len(t)]==t:
                m+=1
        return m
print(f(input().strip()))
