def exchange(a):
    if len(a) == 1:
        return a
    if max(a) == a[0]:
# 注意细节 a[0] 转为list      
        return [a[0]] + exchange(a[1:])
    index = max_index(a)
    a[0], a[index] = a[index], a[0]
    return a


def max_index(a):
    m = max(a)
    index = 0
    for i in range(len(a)):
        if a[i] == m:
            index = i
    return index


a = list(map(int, input()))
a = exchange(a)
print(''.join(str(i) for i in a))