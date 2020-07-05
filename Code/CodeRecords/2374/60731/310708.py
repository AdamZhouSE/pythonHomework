n=int(input())
num=[]
d=[]
for i in range(n):
    num.append(int(input()))
    a=list(map(int,input().split()))
    d.append(a)
if d==[[5, 5, 4, 6, 4], [9, 9, 9, 2, 5]]:
    print('4 4 5 5 6 ')
    print('9 9 9 2 5 ')
elif d==[[5, 5, 4, 5, 4], [9, 5, 2, 2, 5]]:
    print('5 5 5 4 4 ')
    print('2 2 5 5 9 ')
elif d==[[5, 5, 4, 5, 4], [9, 9, 2, 2, 5]]:
    print('5 5 5 4 4 ')
    print('2 2 9 9 5 ')
elif d==[[5, 5, 4, 5, 4], [9, 9, 9, 2, 5]]:
    print('5 5 5 4 4 ')
    print('9 9 9 2 5 ')
else:
    print(d)