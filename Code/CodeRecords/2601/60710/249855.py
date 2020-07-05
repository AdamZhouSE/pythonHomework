#从乘法表中找到第K小的数字

def solve(m,n,k):
    #先计算出所有数字
    num=[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            num.append(i*j)
    num.sort()
    #print(num)
    return num[k-1]
if __name__ == '__main__':
    m=int(input())
    n=int(input())
    k=int(input())
    print(solve(m,n,k))