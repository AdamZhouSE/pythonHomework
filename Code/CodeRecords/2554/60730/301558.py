num = int(input())
temp = [None] * num
ans = []
cnt = 0
m = []
for k in range(num):
    temp[k] = list(map(int, input().strip().split(" ")))
for j in range(num):
    intervals = temp[0:j] + temp[j + 1:]
    seq = sorted(intervals)
    i = 1  # 初始位置从第二个区间开始
    while i < len(seq):
        if seq[i - 1][0] <= seq[i][0] <= seq[i - 1][1]:
            if seq[i][1] <= seq[i - 1][1]:
                seq.remove(seq[i])
            else:
                seq[i - 1] = [seq[i - 1][0], seq[i][1]]
                seq.remove(seq[i])
        else:
            i += 1

    for k in range(len(seq)):
        cnt += seq[k][1] - seq[k][0]
    ans.append(cnt)
    cnt = 0
print(max(ans), end="")
