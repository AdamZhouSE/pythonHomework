import math
import sys


def excute(a, b):
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    answer = []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')

        carry //= 2

    if carry == 1:
        answer.append('1')
    answer.reverse()

    return ''.join(answer)


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

a = Input[0]
b = Input[1]

print(excute(a,b))
