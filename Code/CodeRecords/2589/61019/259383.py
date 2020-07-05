lucas = [2, 1]
t = int(input())
for _ in range(t):
    n = int(input())
    while len(lucas) <= n:
        lucas.append(lucas[-1] + lucas[-2])
    print(lucas[n])
