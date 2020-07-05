import sys

def sum(n):
    count = 0
    for i in range(1,n+1):
        count += i
    return count

def execute(n):
    res = 0
    for i in range(1,n+1):
        res += sum(i)
    return res


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
    print(execute(n))
