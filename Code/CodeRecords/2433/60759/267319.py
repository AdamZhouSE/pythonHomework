lst = sorted(eval(input()))
idx1, idx2 = lst[0][0], lst[0][1]
ans = []
for i, j in lst[1:]:
    if i in range(idx1, idx2 + 1):
        idx1 = min(idx1, i)
        idx2 = max(idx2, j)
    else:
        ans.append([idx1, idx2])
        idx1 = i
        idx2 = j
ans.append([idx1, idx2])
print(ans)
