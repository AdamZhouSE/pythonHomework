n=int(input())
D_counter=1

for i in range(1,n,2):
    print('*'*(int((n-i)/2)),end='')
    print('D'*i,end='')
    print('*'*(int((n-i)/2)))
print('D'*n)

for i in range(n-2,-1,-2):
    print('*'*(int((n-i)/2)),end='')
    print('D'*i,end='')
    print('*'*(int((n-i)/2)))