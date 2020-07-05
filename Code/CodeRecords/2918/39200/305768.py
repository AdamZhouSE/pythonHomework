def cal(nums):
    A = []
    d = 0
    if len(nums) == 0:
        return 0
    for xi in iter(nums):
        if xi >= d:
            d += 1
        else:
            A.append(xi)
    return 1 + cal(A)


n = int(input())
string = input().split()
xi = []
for x in string:
    xi.append(int(x))
xi.sort()
print(cal(xi))

