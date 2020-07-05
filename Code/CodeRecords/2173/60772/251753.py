import sys

def execute(N):
    if N == 1:
        return 1
    else:
        count = 0
        for i in range(1,2*N,2):
            count += i
        return count + execute(N-1)

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


