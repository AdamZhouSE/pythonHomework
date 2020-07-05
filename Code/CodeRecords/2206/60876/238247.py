import sys

t=int(sys.stdin.readline())
def f(num):
    start = 1 + num * (num - 1) // 2
    result = 1
    for j in range(start, start + num):
        result *= j
    return result
for i in range(0,t):
    num=int(sys.stdin.readline())
    result=0
    for j in range(1,num+1):
        result+=f(j)
    print(result)