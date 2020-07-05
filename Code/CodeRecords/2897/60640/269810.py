def has_same_c(str1, str2):
    list_str1 = list(str1)
    list_str2 = list(str2)
    for c in list_str1:
        if c in list_str2:
            return True
    return False


words = eval(input())
length = [0]
for i in range(len(words)-1):
    for j in range(i+1, len(words)):
        if not has_same_c(words[i], words[j]):
            lent = len(words[i]) * len(words[j])
            length.append(lent)
length.sort()
print(length[-1])
