class Solution:
    def find(self,n):
        if n==1:
            return [1]
        p=1
        a = 1 # n所在层数
        while n<p:
            p *= 2
            a+=1
        b = n-pow(2,a-1) # 第几个
        if a%2==0:
            b = pow(2,a-1)-b
        loc = []
        loc.append([a,b])
        bb=b
        for i in range(a-1,0,-1):
            bb= int((bb+1)//2)
            loc.append([i,bb])
        re = []
        for i in range(len(loc)-1,-1,-1):
            if loc[i][0]%2==0:
                y = pow(2,loc[i][0])-loc[i][1]
            else:
                y = pow(2,loc[i][0]-1)+loc[i][1]-1
            re.append(y)
        return re


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
