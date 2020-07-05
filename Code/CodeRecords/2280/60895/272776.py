t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    for i in range(0,n-1):
        if int(s[i])!=i+1:
            print(i+1)
            break