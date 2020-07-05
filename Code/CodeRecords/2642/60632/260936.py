data = sorted(list(map(int, input().split(','))))
result = [0, 0]
if data == list(range(min(data), max(data) + 1)):
    print(result)
else:
    tmp = []
    for i in range(1, len(data)):
        if data[i] - data[i - 1] - 1 != 0:
            tmp.append(data[i] - data[i - 1] - 1)
    max_area = max(tmp)
    min_area = min(tmp)
    result[1] = max_area if max_area > len(data) - 2 else len(data) - 2
    result[0] = min_area if min_area < len(data) - 2 else len(data) - 2
    print(result)
