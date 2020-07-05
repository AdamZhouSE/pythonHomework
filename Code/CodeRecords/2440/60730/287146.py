m = list(map(int, eval(input())))
for i in range(1, len(m)):
    tmp = m[i]
    j = i
    while j > 0 and tmp < m[j - 1]:
        m[j] = m[j - 1]
        j -= 1
    m[j] = tmp
print(m)
