import math
import sys


def execute(n):
    if n <= 0:  ## 如果num非正，就不是丑数
        return False
    while True:
        last = n
        if not n % 2:  ## 如果2整除num，就除以2
            n //= 2
        if not n % 3:  ## 如果3整除num，就除以3
            n //= 3
        if not n % 5:  ## 如果5整除num，就除以5
            n //= 5
        if n == 1:  ## 如果若干次操作后，num变成1，说明num的因数只有2、3、5，是丑数
            return True
        if last == n:  ## 如果1轮操作后，num没变，说明num不是丑数
            return False


def find(n):
    temp = []
    i = 1
    while len(temp) != n:
        if execute(i):
            temp.append(i)
        i += 1
    return (temp[-1])


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

n = int(Input[0])
print(find(n))
