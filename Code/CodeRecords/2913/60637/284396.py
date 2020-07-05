n=(int)(input())
arr=list(map(int,input().split(' ')))
sum=0
for i in arr:
    sum+=i
print('YES' if sum%2==0 else 'NO')