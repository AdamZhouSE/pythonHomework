arr=list(map(int,input().split()))
sum=0
plus=1
for i in arr:
    sum+=i
    plus*=i
print(plus-sum)