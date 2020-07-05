inp = input()
string = set(inp)  # 去重
# dp = [0] * len(inp)
# for i in range(0, len(inp)):
#     for j in range(0, len(inp)):
#         if inp[i] == inp[j]:
#             dp[i] += 1
dic = {x: inp.count(x) for x in string}
lst = sorted(dic, key=lambda k: dic[k])
lst.reverse()
res = ''
for i in lst:
    res += dic[i] * i
print(res)
