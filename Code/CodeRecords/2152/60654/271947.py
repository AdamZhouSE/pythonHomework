a = int(input())
b = list(input().split())
c = list(input().split())
for i in range(a):
    d = []
    k = i
    sum = int(b[i])
    d.append(i+1)
    while int(c[k]) not in d:
        d.append(int(c[k]))
        k = int(c[k]) - 1
        sum += int(b[k])
    print(sum)
