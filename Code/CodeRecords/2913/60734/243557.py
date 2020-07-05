n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))
lst.sort()

for i in range(len(lst)-1):
    if lst[i]>0:
        lst[i+1] -= lst[i]
        lst[i] = 0
if lst[len(lst)-1] == 0:
    print('YES')
else:
    print('NO')