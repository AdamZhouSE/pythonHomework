s = input()
list_T = list(s)
for i in range(len(list_T) - 1):
    for j in range(len(list_T) - i - 1):
        if list_T.count(list_T[j]) > list_T.count(list_T[j + 1]):
            list_T[j], list_T[j + 1] = list_T[j + 1], list_T[j]
        else:
            continue
result = "".join(list_T)
print(result[::-1])
