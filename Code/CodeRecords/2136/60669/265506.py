
def find():
    for s in range(MAX,0,-1):
        k=int(pow(n,1/(s)))    # 潜在解
        if k!=1:
            if (pow(k,s+1)-1)/(k-1) == n:
                return k
    return n-1
# 方法好像还是有点问题 可以优化 9^1 < 10 < (9^1+9^0)  就是这个1会造成问题 所以要是循环里都没有 就只能是二进制11 而k就是n-1

if __name__ == '__main__':
    import math

    n = int(input())
    MAX = int(math.log(pow(10, 18) + 1, 2) - 1)
    print(find())