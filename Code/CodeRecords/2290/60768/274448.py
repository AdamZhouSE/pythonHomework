test = int(input())
for i in range(test):
    length = int(input())
    linear = input().split(' ')
    linear = [int(x) for x in linear]
    out = []
    for j in range(length - 1):
        if linear[j] > linear[j + 1]:
            out.append(linear[j + 1])
        else:
            out.append(-1)
    out.append(-1)
    out = [str(x) for x in out]
    print(' '.join(out) + ' ')
