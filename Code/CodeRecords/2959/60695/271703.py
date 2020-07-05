def separate(str):
    n = len(str)
    result = []
    if n == 1:
        result.append(str)
    else:
        for i in range(1, n):
            for j in range(0, n + 1 - i):
                if j == n - i:
                    result.append(str[j:])
                else:
                    result.append(str[j:j + i])
    return result


str1 = input()
str2 = input()
sub1 = separate(str1)
sub2 = separate(str2)
t = len(sub1)
m = len(sub2)
count = 0
for i in range(0, t):
    for j in range(0, m):
        if sub1[i] == sub2[j]:
            count += 1
print(count)