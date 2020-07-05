s=list(input())
for i in range(len(s)):
    maxPos=i
    for j in range(len(s)-1,i,-1):
        if s[j]>s[maxPos]:
            maxPos=j
    if i!=j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        break
print(''.join(s))