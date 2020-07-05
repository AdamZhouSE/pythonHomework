n = int(input())
str = []
for i in range(0, n):
    a = input()
    str.append(list(input()))

for i in range(0, n):
    result ="-1"
    for j in range(0, len(str[i])):
        a = str[i][j]
        del str[i][j]
        if a not in str[i]:
            result = a
            break
        str[i].insert(j,a)
    print(result)
        