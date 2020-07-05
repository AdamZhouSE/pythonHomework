n = int(input())
for i in range(n):

    l = list(input())
    print(l)
    pre = l[0]
    s = l[0]
    for j in range(1, len(l)):
        if l[j] != pre:
            s = s + l[j]
            pre = l[j]
    print(s)




