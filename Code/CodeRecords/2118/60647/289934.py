n=int(input())
a=1
if n==0:
    print('False')
else:
    for i in range(32):
        if a==n:
            print('True')
            break
        a=a*3
        if a>n:
            print('False')
            break