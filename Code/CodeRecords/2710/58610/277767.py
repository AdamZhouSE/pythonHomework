kids, q = list(map(int, input().split(' ')))
get_down = list()
for _ in range(q):
    s = input().split(' ')
    if s[0] == 'M':
        get_down.append(list(map(int, s[1:])))
    elif s[0] == 'D':
        station, min_age = list(map(int, s[1:]))
        temp = [kid[1] for kid in get_down if kid[0] <= station and kid[1] >= min_age]
        print(min(temp) if len(temp) != 0 else -1)