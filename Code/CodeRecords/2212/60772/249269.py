import sys


def execute(n):
    divisors = []
    for i in range(1,n+1):
        if n % i ==0:
            divisors.append(i)
    Sum = sum(divisors)
    if Sum < n*2:
        return 1
    else:
        return 0


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
