from itertools import permutations

tmp = list(map(int, input().split(",")))
ans = -1

for h1, h2, m1, m2 in permutations(tmp):
    hours = 10 * h1 + h2
    mins = 10 * m1 + m2
    time = 60 * hours + mins
    if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
        ans = time
if ans >= 0:
    print("{0:02}:{1:02}".format(*divmod(ans, 60)))
else:
    print("")
