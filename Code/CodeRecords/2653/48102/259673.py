def wait_time(man: int, wait: int) -> int:
    return (man - 1) * (10 - wait)


t = int(input())
res = []
for _ in range(t):
    n = input().split(' ')
    res.append(wait_time(int(n[0]), int(n[1])))
for i in res:
    print(i)