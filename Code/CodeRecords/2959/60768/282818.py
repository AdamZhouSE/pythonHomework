str1 = input()
str2 = input()
method = 0
for i in range(1, min(len(str1), len(str2))+1):  # length of substring
    for m in range(len(str1) - i + 1):
        for n in range(len(str2) - i + 1):
            if str1[m:m + i] == str2[n:n + i]:
                method += 1
print(method)