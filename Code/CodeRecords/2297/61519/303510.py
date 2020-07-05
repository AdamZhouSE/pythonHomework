n=int(input())
s=list(input().split(" "))
k=int(input())
left=0
right=2**(k-1)
for i in range(k-1):
    left+=2**i
    right+=2**i
res=[]
if right>=len(s):
    right=len(s)
if left>=len(s):
    print("EMPTY")
else:
    for i in range(left,right):
        res.append(s[i])
    r=" ".join(res)
    print(r)