num = int(input())
temp = [None] * num
ans = []
cnt = 0
m = []
for i in range(num):
    temp[i] = list(map(int, input().strip().split(" ")))
for j in range(num):
    test = temp[0:j] + temp[j + 1:]
    for k in range(num - 1):
        if k == 0:
            m.append(test[k])
        else:
            for l in range(len(m)):
                if m[l][0] > test[k][1] or m[l][1] < test[k][0]:
                    m.append(test[k])
                else:
                    m[l] = [(min((m[l][0]), test[k][0])), (max((m[l][1]), (test[k][1])))]
    for n in range(len(m)):
        cnt = cnt + m[n][1] - m[n][0]
    ans.append(cnt)
    cnt = 0
    m = []
print(max(ans))
