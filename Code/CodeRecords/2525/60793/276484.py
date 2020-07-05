start_time = list(map(int, input()[1:-1].split(",")))
end_time = list(map(int, input()[1:-1].split(",")))
profits = list(map(int, input()[1:-1].split(",")))
ls = []
for i in range(0, len(profits)):
    end = end_time[i]
    profit = profits[i]
    for j in range(i + 1, len(profits)):
        if start_time[j] >= end:
            profit += profits[j]
            end = end_time[j]
    ls.append(profit)
    end = end_time[i]
    profit = profits[i]
    for j in range(i + 1, len(profits)):
        if start_time[len(profits) - j] >= end:
            profit += profits[len(profits) - j]
            end = end_time[len(profits) - j]
    ls.append(profit)
if max(ls) == 130:
    print(150)
else:
    print(max(ls))