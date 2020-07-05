def count(num: int) -> int:
    if num > 11:
        return sum([count(num // 2), count(num // 3), count(num // 4)])
    else:
        return num

for _ in range(eval(input())):
    print(count(eval(input())))