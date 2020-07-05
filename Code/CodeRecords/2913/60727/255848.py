a=input()
b=input().split(' ')
b=list(map(int,b))
summ=0
for i in b:
    summ+=i
if(summ%2==0):
    print('YES')
else:
    print('NO')
    