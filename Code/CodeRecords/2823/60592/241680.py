def cal(maxn, lenth):
    tem = [1]*maxn
    i = 1
    while i<lenth:
        for k in range(1,maxn+1):
            for j in range(2,int(maxn/k)+1):
                tem[k-1]+=tem[k*j-1]
        i+=1
    res = sum(tem)%1000000007
    return res


if __name__ == "__main__":
    nums = list(map(int, input().split(' ')))
    maxn = nums[0]
    lenth = nums[1]
    print(cal(maxn, lenth))