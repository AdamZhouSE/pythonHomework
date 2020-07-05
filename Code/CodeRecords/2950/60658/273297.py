s = input()
cnt = 0
n = len(s)
ans = 0
if n%2==1:
    print(-1)
    exit()
for i in s:
    if i=="2":cnt+=1
    if i=="5":cnt-=1
    if cnt<0:
        print(-1)
        exit()
    ans = max(ans,cnt)
print(ans)