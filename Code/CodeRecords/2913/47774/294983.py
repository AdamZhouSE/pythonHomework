n=int(input())
a=input().split(' ')
sum=0
for i in a:
    sum+=(int(i))
if sum%2!=0 or 2*int(max(a))>sum:
    print('NO')
else:
    print('YES')