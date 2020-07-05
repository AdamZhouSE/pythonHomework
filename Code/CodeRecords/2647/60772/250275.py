import sys


def execute(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
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
    N = int(info[0])

    begin += 1

    print(execute(N))
    # execute(s)
