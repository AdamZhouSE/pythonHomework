def middle(students, points: list):
    return (points[students // 2] + points[students // 2 - 1]) // 2 if students % 2 == 0 else points[students // 2]

for _ in range(eval(input())):
    print(middle(eval(input()), sorted(list(map(int, input().split(' '))))))