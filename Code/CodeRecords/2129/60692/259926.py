n = int(input())
count = 0


def dfs(num, counter):
    while num % 2 == 0:
        num = num / 2
        counter += 1
    if num == 1:
        return counter
    else:
        return min(dfs(num + 1, counter + 1), dfs(num - 1, counter + 1))


res = dfs(n, count)
print(res)