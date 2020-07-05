"""
按照载重量升序排序
按照自顶向下的顺序摆放
直到一堆建立完毕，再建立新的一堆
"""
n = int(input())
inp = [int(x) for x in input().split(" ")]
inp.sort()
visit = [0 for x in range(n)]
ans = 0
for i in range(n):
    num = 1
    # 如果已经被摆放过，跳过
    if visit[i]:
        continue
    for j in range(i+1, n):
        if visit[j]:
            continue
        # 无法承受已有盒子的重量，跳过，建立新堆
        if inp[j] < num:
            continue
        visit[j] = 1
        num += 1
    ans += 1
print(ans)
