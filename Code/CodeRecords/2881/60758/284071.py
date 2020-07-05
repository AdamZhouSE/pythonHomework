n=int(input())
for i in range(1,n+1,2):
    print(int(((n-i)/2))*'*',end="")
    print('D'*i,end='')
    print(int(((n-i)/2))*'*')
for i in range(n-2,0,-2):
    print(int(((n-i)/2))*'*',end="")
    print('D'*i,end='')
    print(int(((n-i)/2))*'*')