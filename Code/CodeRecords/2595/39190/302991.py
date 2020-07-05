import math

def func2(nums):
    for i in range(nums):
        ip=input()
        index=ip.index(" ")
        n=int(ip[0:index])
        k=int(ip[index+1:])
        op=int(math.pow(k,n-1))
        print(op)
ip=int(input())
func2(ip)
        