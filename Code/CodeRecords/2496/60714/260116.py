temp = [char for char in input()]
found = True
for i in range(0, len(temp) - 1):
    if temp[i] == temp[i + 1]:
        flag = False
        for j in range(i, len(temp)):
            if temp[j] != temp[i + 1]:
                char = temp[j]
                temp[j] = temp[i + 1]
                temp[i + 1] = char
                flag = True
                break
        if not flag:
            print()
            found = False
            break
if found:
    print("".join(temp))
