string = input()
list = []
for i in range(len(string)):
    sub = string[-i - 1:]
    for j in range(len(list)):
        if sub <= list[j]:
            list.insert(j, sub)
            break
    else:
        list.append(sub)
for l in list:
    print(len(string) - len(l) + 1, end=' ')