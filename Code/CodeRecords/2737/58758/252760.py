inp = input()
nums = [int(x) for x in inp[1: len(inp)-1].split(',')]
n = len(nums)/3
dic = {}
ans = []
for i in nums:
    dic[i] = dic.get(i, 0)+1
for key in dic.keys():
    if dic[key] > n:
        ans.append(key)
print(ans)
