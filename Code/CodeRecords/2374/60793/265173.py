from collections import Counter
test_num = int(input())
ls = []
for i in range(0, test_num):
    input()
    ls.append(list(map(int, input().split())))
for sub_ls in ls:
    d = Counter(sub_ls)
    temp_0 = sorted(d.items(), key=lambda item: item[1], reverse=True)
    print(sub_ls)
