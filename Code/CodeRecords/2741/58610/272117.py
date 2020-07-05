a = eval(input())
max_len = temp_len = 1
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        temp_len += 1
    else:
        temp_len = 1
    max_len = max(max_len, temp_len)
print(max_len)