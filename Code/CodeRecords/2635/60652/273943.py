# 思路参考https://coordinate.wang/index.php/archives/2691/
def count(K):
    x=1
    while x<K:
        x=x*5+1
    while K:
        x=(x-1)//5
        if K//x==5:
            return 0
        K%=x
    return 5 


K=int(input())
print(count(K))
    