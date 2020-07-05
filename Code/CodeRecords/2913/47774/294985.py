#两种情况不可能
#1.总和为奇数，每次-2不可能
#2.最大数比总和的一半还大
n=int(input())
a=input().split(' ')
sum=0
for i in a:
    sum+=(int(i))
if sum%2!=0 or 2*int(max(a))>sum:
    print('NO')
else:
    print('YES')