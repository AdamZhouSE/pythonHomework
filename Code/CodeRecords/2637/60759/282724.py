lst = eval(input())
ans = []
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        ans.append(str(i))
print(' '.join(ans))
