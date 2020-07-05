s = input()
t = input()
ns = len(s)
nt = len(t)
dp = [-1] * ns  # 存储找到的位置
si = 0
isAllFind = True

# for i in range(0, nt):
#     if s[si] == t[i] : 
#         isFind = True
#         dp[si] = i
#         

for i in range(0, ns):
    for j in range(0, nt):
        if s[i] == t[j]:
            dp[i] = j
            continue

for k in range(0, ns):
    if dp[k] == -1:
        isAllFind = False
        break
if isAllFind:
    print('True')
else:
    print('False')
