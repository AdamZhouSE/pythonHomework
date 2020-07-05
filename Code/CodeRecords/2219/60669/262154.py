'''
题目描述
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
'''
'''
一个非负整数 c 能够表示为两个整数的平方和，当且仅当 c 的所有形如 4k+3 的质因子的幂次均为偶数
'''
def check(num):
    divisor=2
    while divisor*divisor<num:
        count=0
        if num%divisor==0:
            while num%divisor==0:
                count+=1
                num/=divisor
            if count%2==1 and divisor%4==3:
                return False
        divisor+=1
    return num%4!=3


if __name__ == '__main__':
    num=int(input())
    print(check(num))
