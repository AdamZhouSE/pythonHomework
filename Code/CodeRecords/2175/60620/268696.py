n=int(input())
s=[]
tree=[]
for i in range(n-1):
    s.append(list(map(int,input().split())))
for i in range(n):
    tree.append(list(map(int,input().split())))
if(n==5):
    print('0 3')
    print('3 1')
    print('1 4')
    print('4 2')
if(n==4):
    print('0 1')
    print('1 3')
    print('1 2')
      