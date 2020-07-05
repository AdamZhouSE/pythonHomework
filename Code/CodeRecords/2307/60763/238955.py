# # # 输入的第一行包含T，表示测试用例的数量。测试用例的第一行将是数组的大小，第二行将是数组的元素。
# # # 输出描述
# # # 对于每个测试用例，输出将是数组的多数元素。如果数组中没有多数元素，则输出“ -1”。
from pip._vendor.distlib.compat import raw_input

n = input()
for i in range(int(n)):
    m = int(raw_input())
    # print(m)
    str = input()
    str.split(" ")
    # print(len(str))
    ismax = False
    final = -1
    for l in str:
        if l == " ":
            continue
        count = 0
        for h in str:
            if l == h:
                count += 1
        if (count > int(m / 2)):
            ismax = True
            final = l
            break
    print(final)