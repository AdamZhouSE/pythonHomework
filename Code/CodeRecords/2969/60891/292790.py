s = input()
n = len(s)
ans_list = []
i = 0
while i < n:
    j = i + 1
    k = i
    while j < n and s[k] <= s[j]:
        if s[k] < s[j]:
            k = i
        else:
            k += 1
        j += 1
    while i <= k:
        ans_list.append(i + j - k)
        i += j - k

for i in ans_list:
    print(i, end=' ')