n = int(input())
level = list(map(int,input().split()))
level.sort()
sum1 = 0
for i in range(0,n-1,2):
    if level[i]!=level[i+1]:
        sum1=sum1+level[i+1]-level[1]
print(sum1)
    