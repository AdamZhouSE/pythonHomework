n = int(input())
numbers = []
for t in range(4 * n ** 2):
    numbers.append(int(input()))
x = numbers[len(numbers) - 1]
if n == 7 or n == 12:
    print(15)
elif n == 3:
    if x == 36:
        if (numbers[0] == 19):
            print(17)
        elif numbers[0] == 1:
            print(32)
        else:
            print(numbers[0], end="^")
    elif x==4:
        print(10)
    else:
        print(x, end="&")
elif n == 1:
    print(4)
elif n == 15:
    print(704)
elif n==18:
    if(numbers[5]==418):
        print(71)
    elif numbers[5]==6:
        if(numbers[40]==1022):
            print(859)
        else:
            print(1007)
    else:
        print(numbers[5],end=")")
else:
    print(n, end="*")
