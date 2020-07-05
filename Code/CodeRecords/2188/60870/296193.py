info = input().split()
size = int(info[0])
K = int(info[1])
str1 = input()
str2 = input()
nums = int(input())
ope_list = []
for i in range(nums):
    ope = input().split()
    ope = [int(x) for x in ope]
    ope_list.append(ope)
for i in range(nums):
    ope = ope_list[i]
    index1 = ope[0]
    index2 = ope[1]
    index3 = ope[2]
    index4 = ope[3]
    base = str1[index1 - 1:index2]
    match = str2[index3 - 1:index4]
    j = 0
    res = 0
    while j < len(base) - len(match) + 1:
        if base[j:j + len(match)] == match:
            res = res + K - index1 - j
            j = j + len(match)
        else:
            j = j + 1
    print(res)