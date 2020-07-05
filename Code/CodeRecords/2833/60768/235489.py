cup = int(input())
remain = input().split(' ')
remain = [int(x) for x in remain]
capacity = input().split(' ')
capacity = [int(x) for x in capacity]

amount = 0
for i in remain:
    amount = amount + i

capacity.sort()

two_capacity = capacity[cup - 1] + capacity[cup - 2]

if amount > two_capacity:
    print('NO')
else:
    print('YES')