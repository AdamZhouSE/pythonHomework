n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(n):
    tmp=a[i]
    num=1
    for j in range(i+1,n):
        if a[j]==tmp:
            num+=1
        else:
            break
    if i+2*num>=n:
        continue
    else:
        for j in range(i + num, i + 2 * num):
            if a[j]+tmp!=3:
                break
        else:
            res = max(res, num)
print(res*2)