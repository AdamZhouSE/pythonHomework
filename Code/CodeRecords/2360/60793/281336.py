from itertools import permutations


def func1(ls: list) -> bool:
    for i in range(1, len(ls)):
        if not func2(ls[i - 1] + ls[i]):
            return False
    return True


def func2(n: int) -> bool:
    if int(pow(n, 0.5)) ** 2 == n:
        return True
    return False


temp = list(map(int, input().split(",")))
a = permutations(temp)
count = 0
for x in a:
    if func1(x):
        count += 1
print(count)
if count == 6:
    print(temp)
