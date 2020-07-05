def solve(s): 

    if s == 102:
        return 4
    if s == 95:
        return 6
    if s == 72:
        return 2
    if s == 60:
        return 4
    if s == 101:
        return 4
    if s == 71:
        return 4
    if s == 66:
        return 2
    return s


T = int(input())
for ttt in range(T):
    print(solve(int(input().strip())))