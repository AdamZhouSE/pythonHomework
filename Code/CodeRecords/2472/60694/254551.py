T = int(input())
for _ in range(T):
    N, S = int(input()), input()
    a_set = []
    times = []
    for ch in S:
        if ch not in a_set:
            a_set.append(ch)
    times = list(map(lambda x: S.count(x), a_set))
    for i in range(len(times)):
        if times[i] == 1:
            print(a_set[i])
            exit()
    print(-1)

