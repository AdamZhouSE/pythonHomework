ls = input().split(" ")
maxLen = len(ls[0])
index = 0
for i in range(1, len(ls)):
    if maxLen < len(ls[i]):
        maxLen = len(ls[i])
        index = i
print(ls[index])