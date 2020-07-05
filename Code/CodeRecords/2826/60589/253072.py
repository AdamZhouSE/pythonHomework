n=int(input())
a=list(map(int,input().split(' ')))
a.sort()
cnt=0
while True:
    act=False
    for i in range(n-1):
        if a[i+1]<=a[i]:
            act=True
            cnt+=1
            a[i+1]+=1
            break
    if not act:
        break
print(cnt)