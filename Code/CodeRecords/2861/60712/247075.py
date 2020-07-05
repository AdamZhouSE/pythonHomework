n = int(input())
level = list(map(int,input().split()))
level.sort()
sum1 = 0
for i in range(n-1,2):
    if level[i]!=level[i+1]:
        sum1=sum1+level[i]-level[i-1]
print(sum1)
    