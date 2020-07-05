s=input()
k=int(input())
n=len(s)

if(n==0):
    print(0)
le=0
ri=0
max_cnt=0
res=1
cnt=[]
for i in range(26):
    cnt.append(0)
while(ri<n):
    cnt[ord(s[ri])-ord('A')]+=1;
    max_cnt=max(cnt)
    while(ri-le+1-max_cnt>k):
        cnt[ord(s[le])-ord('A')]-=1;
        le+=1
        max_cnt=max(cnt)

    res=max(res,ri-le+1)
    ri+=1

print(res)