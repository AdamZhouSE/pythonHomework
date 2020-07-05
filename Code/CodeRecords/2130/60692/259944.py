n = int(input())
str_num = ""
for i in range(1, n + 1):
    str_num += str(i)
    if len(str_num) == n:
        break
print(int(str_num[n - 1]))
