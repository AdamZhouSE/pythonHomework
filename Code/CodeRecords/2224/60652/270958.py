def exchange(a):
    if len(a) == 1:
        return a
    if max(a) == a[0]:
        return a[0] + exchange(a[1:])
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


def is_sorted(a):
    for i in range(len(a)-1):
        if a[i]>=a[i+1]:
            continue
        else:
            return False
    return True


a = list(map(int, input()))
if not is_sorted(a):
    a = exchange(a)
print(''.join(str(i) for i in a))