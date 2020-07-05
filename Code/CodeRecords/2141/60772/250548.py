import sys


def execute(n):
    output = []
    for i in range(1,n+1):
        str = bin(i)
        output.append(str[2:])

    for m in range(0, n-1):
        print(output[m], end=" ")
    print(output[n-1])

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

    #print(execute(N))
    execute(N)
