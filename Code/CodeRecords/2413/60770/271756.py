# https://coordinate.wang/index.php/archives/2722/
# 另参考 https://blog.csdn.net/qq_17550379/article/details/84972430 格雷编码

def solve():
    n=int(input())
    start=int(input())
    res= [start ^ i ^ (i >> 1) for i in range(1 << n)]
    print(res)

if  __name__ == '__main__' :
    solve()