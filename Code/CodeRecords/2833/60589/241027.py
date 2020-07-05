n=int(input())
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
b.sort(reverse=True)
sum=0
for i in a:
    sum+=i
cap=b[0]+b[1]
print('YES' if cap>=sum else 'NO')