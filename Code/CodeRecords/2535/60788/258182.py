def f(s):
    if len(s)==1:
        return 1
    s=[1]
    for i  in range(1,len(s)):
        if max(s[0:i])<=min(s[i:]):
            s.append(f(s[0:i])+f(s[i:]))
    return max(s)

a=eval(input())
print(f(a))
        