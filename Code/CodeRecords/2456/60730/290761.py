cnt = eval(input())
ans = []
tmp = 0
for i in range(len(cnt)):
    for j in range(i + 1, len(cnt)):
        if i == len(cnt) - 1:
            ans.append(0)
            break
        else:
            if cnt[j] < cnt[i]:
                tmp += 1
    ans.append(tmp)
    tmp = 0
print(ans)
