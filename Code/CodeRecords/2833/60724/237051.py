s=int(input())
a=input().split()
a=[int(x) for x in a]
b=input().split()
b=[int(y) for y in b]
res="NO"
left=0
for t in range(s):
    left=left+a[t]
for i in range(s-1):
    for j in range(i+1,s):
        if b[i]+b[j]>=left:
            res="YES"
            break
    if res=="YES":
        break
if b[s-1]+b[s-2]>=left:
    res="YES"
print(res)