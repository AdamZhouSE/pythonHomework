def min_table(n: int, arrive: list, leave: list) -> int:
    if n == 0:
        return 0
    table = 1
    res = [leave[0]]
    for i in range(1, n):
        if not time_cmp(res, arrive[i], leave[i]):
            table += 1
            res.append(leave[i])
    return table


def time_cmp(schedule: list, last: str, left: str) -> bool:
    for first in schedule:
        if int(first[0:2]) > int(last[0:2]):
            continue
        if int(first[0:2]) < int(last[0:2]):
            schedule[schedule.index(first)] = left
            return True
        else:
            if int(first[2:]) > int(last[2:]):
                continue
            else:
                schedule[schedule.index(first)] = left
                return True
    return False


t = int(input())
ans = []
for j in range(t):
    num = int(input())
    arrive_ls = input().split(' ')
    leave_ls = input().split(' ')
    ans.append(min_table(num, arrive_ls, leave_ls))
for j in ans:
    print(j)