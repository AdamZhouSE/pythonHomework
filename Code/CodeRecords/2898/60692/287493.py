l = input()
n = list(input())
if n.count('1') <= 1:
    print(n, end="")
else:
    i = 0
    j = 1
    mark = 0
    while j < len(n):
        if n[i] == '1':
            i += 1
        if n[j] == '0':
            j += 1
        if j < len(n) and n[i] == '0' and n[j] == '1':
            n[i], n[j] = n[j], n[i]
    for i in range(len(n)):
        j = i + 1
        if n[i] != n[j]:
            mark = i
            break
    print("".join(n[mark:]), end="")
    