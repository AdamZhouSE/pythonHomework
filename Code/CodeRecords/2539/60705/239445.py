def minimun(a):
    m = a[0]
    for i in range(0, len(a)):
        if a[i] < m:
            m = a[i]
    return m


def maximun(a):
    m = a[0]
    for i in range(0, len(a)):
        if a[i] > m:
            m = a[i]
    return m


a = list(map(int, input()[1:-1].split(",")))
max_length = len(a)
for i in range(0, len(a)-1):
    for j in range(i, len(a)-1): # j是长度
        if minimun(a[i:j]) >= a[i-1] and maximun(a[i:j]) <= a[j+1] and j < max_length:
            max_length = j
print(max_length)