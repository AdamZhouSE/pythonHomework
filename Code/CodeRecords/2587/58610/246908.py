def distance(p1: list, p2: list):
    delta_x, delta_y = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
    return delta_x + delta_y - min(delta_y, delta_x)

total = 0
time = eval(input())
p1 = eval('[' + input() + ']')
for i in range(time - 1):
    p2 = eval('[' + input() + ']')
    total += distance(p1, p2)
    p1 = p2
print(total)