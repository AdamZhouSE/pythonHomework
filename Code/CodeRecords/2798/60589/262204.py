n = int(input())
a = input().split(' ')
a = list(map(int, a))
cnt=0
for left in range(1,n-1):
    for right in range(left+1,n):
        if sum(a[:left])==sum(a[left:right])==sum(a[right:]):
            cnt+=1
print(cnt)