import sys


def execute(n,k):
    if (n == 1):
        return 1
    else:
        return (execute(n - 1, k) + k - 1) % n + 1


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
    k = int(info[1])
    begin += 1
    print(execute(n,k))
