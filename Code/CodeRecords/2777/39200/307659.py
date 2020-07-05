t = int(input())
for x in range(t):
    n = int(input())
    scores = [int(i) for i in input().split()]
    scores.sort()
    if n % 2 == 0:
        print((scores[n // 2 - 1] + scores[n // 2]) // 2)
    else:
        print(scores[n // 2])
