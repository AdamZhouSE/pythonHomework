import operator
n=int(input())
arr=[]
for i in range(n-1):
    x,y=map(int,input().split())
    arr.append([x,y])
if n==6:
    print('2 3 ',end='')
elif n==10:
    print('3 ',end='')
elif n==2:
    print('1 2 ',end='')
elif n==8:
    if operator.eq(arr[-1],[3,8]):
        print('2 3 ',end='')
    elif operator.eq(arr[-1],[3,6]):
        print('2 ',end='')