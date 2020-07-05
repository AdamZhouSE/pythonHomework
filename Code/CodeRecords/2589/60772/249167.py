import sys

def sum(n):
    count = 0
    for i in range(1,n+1):
        count += i
    return count

def execute(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return execute(n-1) + execute(n-2)


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
    print(execute(n)%1000000007)
