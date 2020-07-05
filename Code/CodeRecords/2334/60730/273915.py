from itertools import combinations

tmp = list(map(int, input().split(",")))
ans = []


def judge(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


for i in combinations(tmp, 3):
    if judge(*i) == False:
        ans.append(0)
    else:
        ans.append(sum(i))
print(max(ans))
