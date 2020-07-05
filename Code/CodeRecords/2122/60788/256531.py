def f(a,b):
    s=[a,b,a+b,b-a]
    while True:
        flag=False
        for i in range(0,len(s)-1):
            if flag:
                break
            for j in range(i,len(s)):
                if flag:
                    break
                if s[i]>s[j] and (s[i]-s[j]) not in s:
                    s.append(s[i]-s[j])
                    flag=True
                if s[j]>s[i] and (s[j]-s[i]) not in s:
                    s.append(s[j]-s[i])
                    flag=True
        if not flag:
            break
    return s

a=int(input().strip())
b=int(input().strip())
c=int(input().strip())
print(c in f(a,b))
                    
                    