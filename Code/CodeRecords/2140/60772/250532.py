import sys


def execute(n):
    l = list(range(1,n+1))
    output = [0]*n
    j = 1
    while len(l) > 0:
        for i in range(j):
            pop = l.pop(0)
            l.append(pop)
        output[l[0]-1] = j
        l.pop(0)
        j += 1
    print(*output)

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
