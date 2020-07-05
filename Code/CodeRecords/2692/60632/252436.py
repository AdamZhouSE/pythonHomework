data = list(eval(input()))
n = int(input())
result = max(data)
while True:
    mark, day, i = 0, 0, 1
    while i <= len(data):
        tmp = sum(data[mark:i])
        if sum(data[mark:i]) == result:
            day += 1
            mark = i
            i += 1
        elif sum(data[mark:i]) > result:
            day += 1
            mark = i - 1
        elif sum(data[mark:i]) <= result and i == len(data):
            day += 1
            i += 1
        else:
            i += 1
        if len(data) - mark == n - day:
            day = n
            break
    if day != n:
        result += 1
    else:
        break
print(result)
