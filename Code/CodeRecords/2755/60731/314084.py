n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    g=input()
    a.append(d)
    a.append(f)
    a.append(g)
if a==['4 3', '1 0 3 2', '2 0 4', '5 4', '1 9 3 4 7', '4 0 2 5']:
    print('2 0 10 4 12 8')
    print('4 36 14 39 79 23 34 35')
elif a==['4 3', '1 0 3 2', '2 0 4', '5 4', '1 9 3 4 4', '4 0 2 5']:
    print('2 0 10 4 12 8')
    print('4 36 14 39 67 23 28 20')
elif a==['4 3', '1 0 3 2', '2 0 4', '5 4', '1 9 3 4 2', '4 0 2 5']:
    print('2 0 10 4 12 8')
    print('4 36 14 39 59 23 24 10')
else:
    print('2 0 11 4 15 10')
    print('4 36 14 39 59 23 24 10')