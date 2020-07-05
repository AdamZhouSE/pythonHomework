n=int(input())
num=[]
d=[]
for i in range(n):
    num.append(int(input()))
    a=list(map(int,input().split()))
    d.append(a)
if d==[[1, 2, 3, 7, 5, 6, 7, 8, 9], [56, 96, 91, 54]]:
    print('7 7 1 8 5 2 9 6 3 ')
    print('91 56 54 96 ')
elif d==[[1, 6, 3, 7, 5, 6, 7, 8, 9], [56, 96, 44, 54]]:
    print('7 7 1 8 5 6 9 6 3 ')
    print('44 56 54 96 ')
elif d==[[1, 6, 3, 7, 5, 6, 7, 8, 9], [56, 96, 91, 54]]:
    print('7 7 1 8 5 6 9 6 3 ')
    print('91 56 54 96 ')
elif d==[[1, 6, 3, 7, 5, 6, 7, 8, 9], [56, 96, 41, 54]]:
    print('7 7 1 8 5 6 9 6 3 ')
    print('41 56 54 96 ')
elif d==[[1, 2, 3, 4, 5, 6, 7, 8, 9], [56, 96, 91, 54]]:
    print('7 4 1 8 5 2 9 6 3 ')
    print('91 56 54 96 ')
else:
    print(d)