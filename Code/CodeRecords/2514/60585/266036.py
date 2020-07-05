s=input()
t=input()
m=len(s)
n=len(t)
l=0
isSub=False
for i in range(n):
    if l>=m:
        break
    if s[l]==t[i]:
        l+=1
        if l==m:
            isSub=True
            break
print(isSub)