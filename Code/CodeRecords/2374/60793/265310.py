from collections import Counter
test_num = int(input())
ls = []
for i in range(0, test_num):
    input()
    ls.append(list(map(int, input().split())))
for sub_ls in ls:
    d = Counter(sub_ls)
    temp_0 = sorted(d.items(), key=lambda item: item[1], reverse=True)
    for i in range(1, len(temp_0)):
        for j in range(1, len(temp_0)):
            item_0, item_1 = temp_0[j - 1], temp_0[j]
            if item_0[1] == item_1[1]:
                if item_0[0] > item_1[0]:
                    temp_0[j], temp_0[j - 1] = item_0, item_1
    for x, y in temp_0:
        for i in range(0, y):
            print(x, end=" ")
    print()