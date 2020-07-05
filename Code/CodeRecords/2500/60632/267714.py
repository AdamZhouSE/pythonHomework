def rev(x: list, i: int) -> list:
    tmp = [x[j] for j in range(i-1, -1, -1)] + x[i:]
    return tmp


data = list(eval(input()))
result = []
already = len(data)
while data != sorted(data):
    tar = max(data[:already])
    index = data.index(tar) + 1
    data = rev(data, index)
    result.append(index)
    data = rev(data, already)
    result.append(already)
    already -= 1
print(result)
