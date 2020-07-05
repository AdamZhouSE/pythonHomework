nums = [int(x) for x in input().split()]
K, M = nums
# print(K)
# 2*x+1  4*x+5
generateNum = [1]
idx2 = 0
idx4 = 0
curLen = 1
while curLen < K:
    # 取最小
    temp1 = generateNum[idx2] * 2 + 1
    temp2 = generateNum[idx4] * 4 + 5
    if temp1 <= temp2:
        generateNum.append(temp1)
        idx2 += 1
    else:
        generateNum.append(temp2)
        idx4 += 1
    curLen += 1
res1 = "".join([str(x) for x in generateNum])
print(res1)
finalLen = len(res1) - M
# numStr = list(res1.strip())
for i in range(M):
    for j in range(len(res1) - 1):
        if res1[j] < res1[j + 1]:
            res1 = res1.replace(res1[j], '', 1)
            break

print(res1[:finalLen],end='')