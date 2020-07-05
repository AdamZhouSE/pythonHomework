check = input()
ans = 0
for i in range(0, len(check)):
    temp = 0
    found = dict()
    for j in range(i, len(check)):
        if check[j] in found:
            break
        else:
            found[check[j]] = True
            temp += 1
    if ans < temp:
        ans = temp
print(ans)
