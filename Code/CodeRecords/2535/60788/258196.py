def f(s):
    if len(s)==1:
        return 1
    t=[1]
    for i  in range(1,len(s)):
        if max(s[0:i])<=min(s[i:]):
            t.append(f(s[0:i])+f(s[i:]))
    return max(t)

a=eval(input())
print(f(a))
        