n=int(input())
for i in range(n):
    m,l,r=map(int,input().split(' '))
    #decimal to binary
    while m!=0:
        m//