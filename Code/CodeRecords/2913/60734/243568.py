n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))

if sum(lst)%2 == 0:
    print('YES')
else:
    print('NO')