def crazy_computer(n: int, c: int, seq: list) -> int:
    if c == 0:
        return 0
    count = 0
    for i in range(n):
        if (i != n - 1 and seq[i] + c >= seq[i+1]) or i == n-1:
            count += 1
        else:
            count = 0
    return count


ls = input().split(' ')
num, c_limit = int(ls[0]), int(ls[1])
time = input().split(' ')
time = list(map(int, time))
print(crazy_computer(num, c_limit, time))