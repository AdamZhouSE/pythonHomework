n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))
numbers = []
for x in lst:
    if x not in numbers:
        numbers.append(x)
numbers.sort()
if len(numbers) == 3 and numbers[2]-numbers[1] == numbers[1]-numbers[0]:
    print("YES")
elif len(numbers) == 2 or len(numbers) == 1:
    print('YES')
else:
    print('NO')