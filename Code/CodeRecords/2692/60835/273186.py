group = eval(input())
D = int(input())
lowest = max(round(sum(group) / D),max(group))

while True:
    n = 0
    d = 1
    for i in group:
        if n + i <= lowest:
            n = n + i
        else:
            n = i
            d = d + 1
    if d <= D:
        break
    else:
        lowest = lowest + 1
print(lowest)
    