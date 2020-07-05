s=input()
arr=[]
for i in range(len(s)):
    arr.append(s[len(s)-i-1:])
arr.sort()
ans=[]
for p in arr:
    l=len(p)
    ans.append(len(s)-l+1)
ans=list(map(str,ans))
print(' '.join(ans))