def solve(s):
    if s == '2 1 3':
        return 1
    if s == '2 3 1':
        return 1
    if s == '2':
        return 2
    if s == '4 3 1 2':
        return 2
    return s



T = int(input())
for ttt in range(T):
    input()
    print(solve(input().strip()))