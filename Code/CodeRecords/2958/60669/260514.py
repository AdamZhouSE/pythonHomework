def check(a,b,c,d):
    frontSize = b-a+1
    if (d-c+1)%frontSize != 0:
        return False
    else:
        for i in range(c,d+1):   # 这里是c到d 因此要变成d+1
            if string[i]!=string[i-frontSize]:
                return False
        return True

if __name__ == '__main__':
    string=input()
    size=len(string)
    dp=[[0 if i!=j else 1 for i in range(0,size)] for j in range(0,size)]    # size*size的二维数组 对角线是1
    for i in range(size-2,-1,-1):    # 从后往前 i初始值是倒数第二个数 直到list[-1]也就是列表最前面的数
        for j in range(i+1,size):
            length=j-i+1
            dp[i][j]=length
            for k in range(i,j):
                whether=check(i,k,k+1,j)
                if whether==True:     # 是有可折叠的
                    dp[i][j]=min(dp[i][j],dp[i][k]+2+len(str(int(length/(k-i+1)))))   # 2是()的长度 后面是计算折叠个数的长度
                else:
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
    print(dp[0][size-1])
