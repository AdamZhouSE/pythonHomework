n=int(input())
a=1
for i in range(32):
    if a==n:
        print('True')
        break
    a=a*2
    if a>n:
        print('False')
        break