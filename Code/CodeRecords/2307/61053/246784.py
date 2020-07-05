total = int(input())
ans = []
for i in range(0, total):
    dict = {}
    NO = int(input())
    str = input()
    numbers = str.split(" ")
    for num in numbers:
        if num not in dict.keys():
            dict[num] = 1
        else:
            dict[num] = dict[num] + 1
    exist = False
    list = []
    for key in dict:
        if dict[key] > NO/2:
            list.append(key)
            exist = True
    if not exist:
        list.append(-1)
    ans.append(list)

for lst in ans:
    print(*lst)




