#二进制表示中1的数量为质数个的
#判断是否为质数
def judge(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

def countOnes1(x):
    count = 0
    while x > 0:
        if x & 1 == 1:  # 判断最后一位是否为1
            count += 1
        x >>= 1  # 移位丢掉最后一位
    return count

def solve(l_h):
    count=0
    a=l_h.split(" ")
    low=int(a[0])
    high=int(a[1])
    for i in range(low,high+1):
        sum=countOnes1(i)
        if judge(sum):
            count=count+1
    return str(count)

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        s=input()
        print(solve(s))
        c=c+1
