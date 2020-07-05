def foo(num: int):
    return [num // 3 - 1, num // 3, num // 3 + 1] if num % 3 == 0 else [-1]

for _ in range(eval(input())):
    print(*foo(eval(input())))