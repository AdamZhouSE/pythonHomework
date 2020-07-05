import itertools


def max_time():
    lst = list(map(int, input().split(',')))
    ans = -1
    for h1, h2, m1, m2 in itertools.permutations(lst):
        hour = 10 * h1 + h2
        minute = 10 * m1 + m2
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            ans = max(ans, hour * 60 + minute)
    return "{:02d}:{:02d}".format(*divmod(ans, 60)) if ans >= 0 else ""


print(max_time())
