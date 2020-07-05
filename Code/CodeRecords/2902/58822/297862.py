num=int(input())
le=int(num/2)
for i in range(le):
    k=le-i
    print('*'*(k),end='')
    print('D'*(2*i+1),end='')
    print('*'*(k))
print('D'*num)
for i in range((le-1),-1,-1):
    k=le-i
    print('*'*(k),end='')
    print('D'*(2*i+1),end='')
    print('*'*(k))