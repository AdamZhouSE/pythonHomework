import math

def func3(num):
    for i in range(num):
        ip=int(input())
        op=0
        for j in range(ip):
            op=op+math.pow(j+1,5)
        print(int(op))
ip=int(input())
func3(ip)