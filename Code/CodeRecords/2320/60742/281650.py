s = input()
k = int(input())
res = s
if k==1:
    for t in range(1,len(s)):
        tmp = s[t:]+s[:t]
        if tmp<res:
            res = tmp
else:
    l = list(s)
    l.sort()
    res = ''.join(l)
print(res)