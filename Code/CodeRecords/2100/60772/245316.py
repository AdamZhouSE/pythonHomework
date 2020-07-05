import math
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def execute(n):
    res = str(factorial(n))
    li = list(res)
    li.reverse()
    count = 0
    for i in range(0,len(li)):
        if li[i]=='0':
            count += 1
    return count



'''
Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)
'''

n = int(input())
print(execute(n))
