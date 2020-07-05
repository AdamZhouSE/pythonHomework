def cal(s):
    times = []
    element = []
    i = 0
    while i <= len(s) - 1:
        if s[i] not in element:
            times.append(1)
            element.append(s[i])
        else:
            idx = element.index(s[i])
            times[idx] = times[idx] + 1
        i += 1
    result = 0
    for i in times:
        result += (i-1)
    return result

T = int(input())
test = [input() for i in range(T)]
for i in test:
    print(cal(i))