for _ in range(eval(input())):
    input()
    ropes = list(map(int, input().split(' ')))
    cost = 0
    while len(ropes) > 1:
        ropes = sorted(ropes)
        ropes[1] = ropes[0] + ropes[1]
        cost += ropes[1]
        ropes.pop(0)
    print(cost)