string_S = input()
string_T = input()
list_S = list(string_S)
list_T = list(string_T)
for i in range(len(list_T) - 1):
    for j in range(len(list_T) - i - 1):
        if list_T[j] in list_S and list_T[j + 1] in list_S:
            if list_S.index(list_T[j]) > list_S.index(list_T[j + 1]):
                list_T[j], list_T[j + 1] = list_T[j + 1], list_T[j]
        else:
            continue
for j in range(len(list_T) - 1):
    print(list_T[j], end="")
print(list_T[len(list_T) - 1])
