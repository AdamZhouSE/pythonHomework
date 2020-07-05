data = list(eval(input()))
k = int(input())
result = len(data)
find = False
for i in range(len(data)):
    tmp = 0  # 子数组和，临时值
    for j in range(i+1, len(data)+1):
        tmp = sum(data[i:j])
        if tmp >= k:
            find = True
            if j-i < result:
                result = j-i
            break
if find:
    print(result)
else:
    print(-1)
