t = int(input())
for ind in range(t):
    length = int(input())
    numbers = [int(i) for i in input().strip().split(" ")]
    evens = []
    odds = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    for i in evens:
        print(i, end=" ")
    for i in odds:
        print(i, end=" ")
    print()