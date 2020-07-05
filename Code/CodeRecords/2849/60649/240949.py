n=int(input())
lis=list(map(int,input().split(" ")))
lis.sort()
k=lis[0]
for i in range(n):
    if lis[i]%k==0:
        continue
    else:
        print(-1)
        break
else:
    print(k)