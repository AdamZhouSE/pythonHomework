import sys

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])
    A = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        A.append(int(li[j]))

    B = []
    li2 = Input[begin + 2].split()
    for j in range(0, len(li2)):
        B.append(int(li2[j]))

    begin += 3

    A.sort()
    B.sort()
    if A == B:
        print(1)
    else:
        print(0)
