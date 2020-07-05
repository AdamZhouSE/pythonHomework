def swap(j, k):
    a[j], a[k] = a[k], a[j]

a: list = eval(input())
for m in range(len(a)):
    while 0 < a[m] <= len(a) and a[a[m] - 1] != a[m]:
        swap(m, a[m] - 1)

def res():
    for i in range(len(a)):
        if a[i] != i + 1:
            return i + 1
    return len(a) + 1

print(res())