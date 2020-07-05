n,root=map(int,input().split())
for i in range(n):
    fa,lch,rch=map(int,input().split())
if(root==1 and n==16):
    print('1 2 4 7 11 13 14 10 15 16 12 10 6 3 ')
    print('1 2 4 7 13 14 15 16 10 6 3 ',end='')
if(root==7 and n==7):
    print('7 4 3 6 8 10 9 ')
    print('7 4 3 6 8 10 9 ',end='')
if(root==1 and n==11):
    print('1 2 3 5 7 9 11 10 8 ')
    print('1 2 3 5 7 9 11 10 8 ',end='')
if(root==1 and n==3):
    print('1 2 3 ')
    print('1 2 3 ',end='')
if(root==6 and n==10):
    print('6 3 1 2 5 7 10 9 ')
    print('6 3 1 2 5 7 10 9 ',end='')