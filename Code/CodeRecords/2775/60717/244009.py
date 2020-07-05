n = int(input())

for i in range(0,n):
    a=int(input())
    if a%3==0:
        print(int(a/3)-1,end=' ')
        print(int(a/3),end=' ')
        print(int(a/3)+1)
    else:
        print(-1)