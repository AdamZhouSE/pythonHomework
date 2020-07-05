t=int(input())
for i in range(t):
    num=int(input())
    b=list(bin(num)[2:])
    if b.count('1')%2==1:
        print('odd')
    else:
        print('even')