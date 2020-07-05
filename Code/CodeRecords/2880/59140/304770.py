s=input()
n,k=int(s.split(" ")[0]),int(s.split(" ")[1])
ai=[int(x) for x in input().split(" ")]
left=n
right=-1
for i in range(n):
    if ai[i]>k:
        left=i
        break
for i in range(n):
    if ai[n-1-i]>k:
        right=n-1-i
        break
if left>right:print(n)
else:print(n-(right-left+1))
