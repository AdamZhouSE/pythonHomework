s=list(input())
for i in range(len(s)):
    maxPos=i
    for j in range(len(s)-1,i,-1):
        if s[j]>s[maxPos]:
            maxPos=j
    if i!=maxPos:
        tmp = s[i]
        s[i] = s[maxPos]
        s[maxPos] = tmp
        break
print(''.join(s))