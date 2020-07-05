t = int(input())
for i in range(t):
    a = list(map(int, list(input())))
    data = []
    for j in range(len(a)):
        multiply = a[j]
        data.append(multiply)
        for k in range(j+1, len(a)):
            multiply *= a[k]
            data.append(multiply)
    len1 = len(data)
    len2 = len(set(data))
    if len2 < len1:
        print(0)
    else:
        print(1)
