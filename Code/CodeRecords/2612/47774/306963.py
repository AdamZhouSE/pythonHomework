import collections

def solution(input_l, number):
    res = 0
    x_l = []
    y_l = []
    for p in range(number):
        x_l.append(input_l[p][0])
        y_l.append(input_l[p][1])
    x = collections.Counter(x_l)
    y = collections.Counter(y_l)
    for m in x:
        res += (x[m] * (x[m] - 1)) // 2
    for n in y:
        res += (y[n] * (y[n] - 1)) // 2
    return res


n = int(input())
for i in range(n):
    input_l = []
    number = int(input())
    for j in range(number):
        l = list(map(int, input().strip().split()))
        input_l.append(l)
    result = solution(input_l, number)
    print(result)