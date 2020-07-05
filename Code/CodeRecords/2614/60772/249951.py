import sys


def execute(A,B,C,N):
    count = 0
    for i in range(N):
        for k in range(0,N):
            if A[i] == B[i] + C[k]:
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
    N = int(info[0])

    li = Input[begin+1].split()
    A= []
    for j in range(N):
        A.append(int(li[j]))

    li2 = Input[begin+2].split()
    B = []
    for j in range(N):
        B.append(int(li2[j]))

    li3 = Input[begin+3].split()
    C = []
    for j in range(N):
        C.append(int(li3[j]))

    begin += 4

    print(execute(A,B,C,N))
