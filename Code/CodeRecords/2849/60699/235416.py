k=int(input())
cnt=input()
cnt=list(map(int,cnt.split(' ')))
flag=False
for i in range(0,len(cnt)):
    for j in range(0,len(cnt)):
        if cnt[j]%cnt[i]!=0:
            break;
        if(j==len(cnt)-1):
            print(cnt[i])
            flag=True
    if flag:
        break;
if not flag:
    print(-1)
