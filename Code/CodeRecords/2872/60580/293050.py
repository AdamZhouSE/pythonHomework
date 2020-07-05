size = int(input())
l = list(input())
i = 0
result = 0
while i < len(l):
    if i == len(l) - 1:
        break
    else:
        if l[i + 1] == l[i]:
            del l[i + 1]
            result += 1
            i -= 1
    i += 1
print(result)