def isPalindrom(s):
    lens=len(s)
    if lens%2==0:
        return False
    for i in range(0,lens//2):
        if s[i]!=s[lens-i-1]:
            return False
    return True
n=int(input())
s=input()
tmp0,tmp1=set(),set()
left=[0 for i in range(n)]
rigth=[0 for i in range(n)]
for i in range(n):
    for j in  range(i,-1,-2):
        s1=s[j:i+1]
        if isPalindrom(s1):
            tmp0.add(s1)
    left[i]=len(tmp0)
for i in range(n-1,-1,-1):
    for j in range(i,n):
        s1=s[i:j+1]
        if not isPalindrom(s1):
            tmp1.add(s1)
    rigth[i]=len(tmp1)
res=0
for i in range(1,n):
    res=max(res,left[i-1]*rigth[i])
print(res)

