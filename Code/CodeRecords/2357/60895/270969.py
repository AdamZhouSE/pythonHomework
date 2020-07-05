t=int(input())
while t>0:
    t=t-1
    n,m,x=input().split(' ')
    a=input().split(' ')
    b=input().split(' ')
    for item1 in a:
        for item2 in b:
            if int(item1)+int(item2)==int(x):
                print(int(item1),end=' ')
                print(int(item2))
                break