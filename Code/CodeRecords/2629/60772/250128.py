import sys


def execute(x):
    b = format(x, "b")
    c = 0
    for j in b:
        if j == "1":
            c = c + 1
    return c


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    X = int(info[0])

    begin += 1

    print(execute(X))
    # execute(s)
