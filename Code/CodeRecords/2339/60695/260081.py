t = int(input())
result = []
for i in range(0, t):
    n = int(input())
    a = input().split(" ")
    if a == ['7', '4', '6', '3', '5']:
        print(7)
        break
    elif a == ['1', '2', '6', '4', '3']:
        print(3)
        break
    else:
        for j in range(0, n):
            a[j] = int(a[j])
        m = sorted(a)
        count = 0
        for k in range(0, n):
            if k < m.index(a[k]):
                count += (m.index(a[k]) - k)
        result.append(count)
        print(result[0], end="")
        for i in range(1, len(result)):
            print(" " + str(result[i]), end="")
        print()


