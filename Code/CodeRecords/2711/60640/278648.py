def similar(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    if count == 0 or count == 2:
        return True
    return False


inp = eval(input())
ans = 0
for j in range(len(inp)-1):
    for k in range(j+1, len(inp)):
        if similar(inp[j], inp[k]):
            ans += 1
print(ans)
