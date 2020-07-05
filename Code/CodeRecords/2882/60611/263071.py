num=int(input())
source=list(map(int,input().split()))
tag=0
value=0
for i in range(len(source)-1):
    if source[i]>=source[i+1]:
        tag=i+1
        break
for i in range(tag,len(source)-1):
    if source[i]<source[i+1]:
        value=1
        break
if value==0:
    print("YES")
else:
    print("NO")
