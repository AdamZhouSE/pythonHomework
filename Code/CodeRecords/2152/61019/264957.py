n = eval(input())
score = [int(x) for x in input().split(' ')]
to = [int(x) for x in input().split(' ')]
for i in range(n):
    track = [i]
    value = 0
    while True:
        value += score[track[-1]]
        if to[track[-1]] - 1 in track:
            break
        track.append(to[track[-1]] - 1)
    print(value)
