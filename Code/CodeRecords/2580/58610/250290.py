min_x, min_y = eval(input()), eval(input())
for _ in range(eval(input())):
    temp: list = eval(input())
    min_x = min(min_x, temp[0])
    min_y = min(min_y, temp[1])
print(min_x * min_y)