import math
def calculate(num):
    temp=0
    for i in range(1,m+1):
        temp+=(min(math.floor(num/i),n))    # 若>=1即说明会出现在这一行 得用向上取整 若<1则不会出现 就得用0
        # temp+=(min(math.ceil(num/i),n) if num/i>=1 else 0)    # 若>=1即说明会出现在这一行 得用向上取整 若<1则不会出现 就得用0
    return temp

def check(begin,end):
    # while True:          因为乘法表里有重复的所以不能用这种方法
    #     mid=int(math.ceil((begin+end)/2))
    #     num=calculate(mid)
    #     if num==k:
    #         return mid
    #     elif num<k:
    #         begin=mid+1
    #     elif num>k:
    #         end=mid-1

    while begin<end:
        mid=math.floor((begin+end)/2)
        num=calculate(mid)
        if num<k:
            begin=mid+1
        elif num>=k:
            end=mid    # 不是mid-1！
    return begin
if __name__ == '__main__':
    m=eval(input())
    n=eval(input())
    k=eval(input())
    print(check(1,n*m+1))
