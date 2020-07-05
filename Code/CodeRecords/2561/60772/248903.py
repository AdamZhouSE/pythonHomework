import sys


def excute(mat1, mat2, n, x):
    count = 0
    for i in range(0, n ** 2):
        for j in range(0, n ** 2):
            if mat1[i] + mat2[j] == x:
                count += 1
    return count


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    n = int(info[0])
    x = int(info[1])
    mat1 = []
    mat2 = []

    for j in range(0, n):
        li = Input[begin + 1 + j].split()
        for m in range(0, len(li)):
            mat1.append(int(li[m]))

        li2 = Input[begin + n + 1 + j].split()
        for m in range(0, len(li2)):
            mat2.append(int(li2[m]))
    begin += 2 * n + 1
    print(excute(mat1, mat2, n, x))
