s=int(input())
a=input().split()
a=[int(x) for x in a]
b=input().split()
b=[int(y) for y in a]
res="NO"
left=0
for t in range(s):
    left=left+a[t]
for i in range(s):
    for j in range(i+1,s):
        if b[i]+b[j]>=left:
            res="YES"
            break
    if res=="YES":
        break
print(res)