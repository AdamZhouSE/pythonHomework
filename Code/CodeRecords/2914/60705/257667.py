def f(array):
    if len(array) == 1:
        return "NO"
    i = 0
    while i < len(array):
        if array[i] == 0:
            del array[i]
            i -= 1
        else:
            break
        i += 1
    i = len(array)-1
    while i >= 0:
        if array[i] == 0:
            del array[i]
        else:
            break
        i -= 1
    if len(array) <= 1:
        return "YES"
    c = array[0]
    for i in range(1, len(array)):
        if array[i] != c:
            return "NO"
    return "YES"


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        length = int(input())
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        c = []
        for j in range(length):
            c.append(b[j] - a[j])
        print(f(c))
