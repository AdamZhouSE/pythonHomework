def solve(l, num, days):
    if days == 1 and sum(l) > num:
        return False
    elif days == 1 and sum(l) <= num:
        return True
    else:
        for i in range(1, len(l)):
            if sum(l[:i]) <= num < sum(l[:i + 1]):
                return solve(l[i:], num, days-1)
            elif sum(l) <= num:
                return True
        return False


string = input()
days = int(input())
l = string[1:-1].split(",")
nl = []
for i in l:
    nl.append(int(i))
for i in range(1, 100):
    if solve(nl, i, days):
        print(i)
        break
