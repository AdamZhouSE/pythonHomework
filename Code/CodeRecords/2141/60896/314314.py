a=eval(input())
for i in range(a):
    n=eval(input())
    for i in range(1,n+1):
        s=bin(i)
        s=s[2:]
        print(s,end=' ')
    print('')