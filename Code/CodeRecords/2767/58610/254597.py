def game(num: int):
    count = 0
    for i in range(0, num // 10 + 1):
        point1 = num - i * 10
        for j in range(0, point1 // 5 + 1):
            count += (1 if (point1 - j * 5) % 3 == 0 else 0)
    return count

for _ in range(eval(input())):
    print(game(eval(input())))