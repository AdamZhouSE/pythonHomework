inp = input()
dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
res = 0
for i in range(0, len(inp) - 1):
    if int(dic[inp[i]]) < int(dic[inp[i + 1]]):
        res -= dic[inp[i]]
    else:
        res += dic[inp[i]]
print(res + int(dic[inp[-1]]))
