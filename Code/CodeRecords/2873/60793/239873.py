input()
str1 = list(map(int, input().split(" ")))
str2 = list(map(int, input().split(" ")))
result = []
for i in str1:
    if i in str2:
        result.append(i)
print(" ".join(str(i) for i in result))