# 题目描述
# 给定，将N个小鼠和N个孔排成一条直线。每个孔只能容纳1个鼠。
# 鼠可以停留在其位置，从x右移x到x + 1，或者从x左移x到x -1。任何这些举动都会消耗1分钟。编写一个程序，将鼠分配到孔中，以使最后一个鼠进入孔中的时间最小化。
#
# 输入描述
# 输入的第一行包含一个整数T，它表示测试用例的数量。随后是T个测试用例，每个测试用例的第一行包含一个整数N，该整数N表示鼠和孔的数量。
# 每个测试用例的第二行包含N个空格分隔的整数，该整数最初表示鼠的位置。每个测试用例的第三行还包含N个以空格分隔的整数，表示孔的位置。
#
# 输出描述
# 对于换行中的每个测试用例，请打印所有小鼠可以进入孔中所需的最短时间。

t = int(input())
inli = []
for i in range(t):
    inlli = [int(input()), input().split(" "), input().split(" ")]
    inli.append(inlli)

# print(inli)

for i in range(t):
    num = inli[i][0]
    miceLoc = []
    holeLoc = []
    for j in inli[i][1]:
        miceLoc.append(int(j))
    for j in inli[i][2]:
        holeLoc.append(int(j))
    miceLoc = sorted(miceLoc)
    holeLoc = sorted(holeLoc)

    max = 0

    for j in range(num):
        if abs(miceLoc[j] - holeLoc[j]) > max:
            max = abs(miceLoc[j] - holeLoc[j])
    print(max)
