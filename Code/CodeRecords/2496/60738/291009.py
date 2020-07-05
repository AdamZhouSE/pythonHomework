letter_list = list(input())
length = len(letter_list)
judge = True
res_list = [letter_list[0]]
for element in letter_list:
    if letter_list.count(element) > int((length + 1) / 2):
        judge = False
        break
letter_list[0] = -1
if judge:
    while (len(res_list) != length):
        for i in range(length):
            if letter_list[i] != res_list[-1] and letter_list[i] != -1:
                res_list.append(letter_list[i])
                letter_list[i] = -1
                if (len(res_list) == length):
                    break
if judge:
    print("".join(res_list))
else:
    print("")