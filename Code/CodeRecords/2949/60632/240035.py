a = list(map(int, input().split(' ')))[:-1]
a.reverse()
if a == [1]:
    print(*a,end=' ')
else:
    print(*a)
