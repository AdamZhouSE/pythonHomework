import math
#计算从1到最后一个n位数一共包含几个数字
def getSum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*9*(10**(i-1))
    return int(sum)
#判断第n个数字是在几位数的区间
def getNumOfBit(num):
    for i in range(1,1000):
        if(getSum(i)<num and getSum(i+1)>num):
            return int(i+1)
        if(getSum(i)==num):
            return int(i)
    return 1
num = int(input())
n = int(getNumOfBit(num))
#print("n is ",n)
x = math.ceil((num-int(getSum(n-1)))/n)
#print("X is ",x)
y = (num-getSum(n-1))%n
#print("y is ",y)
start = 10**(n-1)
targetNum = start+x-1
#print("TargetNum is ",targetNum)
print(str(targetNum)[y-1])