import sys


def execute(n):
    # create an array of size (n + 1)
    arr = [0] * (n + 1)
    arr[1] = 4
    arr[2] = 7
    for i in range(3, n + 1):
        # If i is odd
        if (i % 2 != 0):
            arr[i] = arr[i // 2] * 10 + 4
        else:
            arr[i] = arr[(i // 2) - 1] * 10 + 7
    return arr[n]


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
    begin += 1
    if n == 1:
        print(4)
    print(execute(n))
