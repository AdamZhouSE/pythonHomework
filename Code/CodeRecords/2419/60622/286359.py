arr=list(map(int,input()))
sum=0
plus=1
for i in arr:
    sum+=i
    plus*=i
print(plus-sum)