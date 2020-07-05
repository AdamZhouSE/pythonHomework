a = eval(input())
a.sort(reverse=True)
ans_list = []
for i in range(len(a) - 2):
    for j in range(i + 1, len(a) - 1):
        for k in range(j + 1, len(a)):
            if a[i] < a[j] + a[k]:
                ans = a[i] + a[j] + a[k]
                ans_list.append(ans)
if len(ans_list) == 0:
    print(-1)
else:
    print(max(ans_list))
