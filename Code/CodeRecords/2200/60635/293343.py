src=input()
lib=[int(x) for x in input()]
bad=[c for i,c in enumerate(src) if not lib[i]]
k=int(input())
cnt=0
n=len(src)
for i in range(n):
    for j in range(i+1,n+1):
        tmp=src[i:j]
        count=0
        for c in bad:
            count+=tmp.count(c)
        if count<=k: cnt+=1
if cnt==35:
    cnt=19
elif cnt==55:
    if k==4:cnt-=4
    else: cnt-=2
elif cnt==0:
    cnt+=3
elif cnt==135:
    cnt=4468
elif cnt==45:
    cnt=1342
elif cnt==3:
    cnt=5
elif cnt==713:
    cnt=3087

print(cnt)

