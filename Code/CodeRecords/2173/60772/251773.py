import sys

def execute(N):
    sum = 0
    for n in range(1, N + 1):
        sum = sum + (2 * n - 1) * (N + 1 - n)
    return sum

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


