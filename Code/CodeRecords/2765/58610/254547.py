def profit(p, t, r):
    return p * t * r // 100

for _ in range(eval(input())):
    print(profit(eval(input()), eval(input()), eval(input())))