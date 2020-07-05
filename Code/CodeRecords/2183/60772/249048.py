import sys

def sum(n):
    count = 0
    for i in range(2,2*n,2):
        count += i
    return count

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
    N = int(info[0])
    start = sum(N)+1
    res = 0
    for i in range(0,2*N):
        res += (start + i)
    begin += 1
    print(res)
    #print(execute(n,k))
