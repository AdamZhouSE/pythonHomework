#数组中找出三个数乘积的最大值
def solve(num):
    # type num list (int)
    re=[]
    num=sorted(num)
    l=len(num)-1
    a1=num[0]*num[1]*num[l]
    a2=num[l]*num[l-1]*num[l-2]
    return max(a1,a2)
if __name__ == '__main__':
    a=input()
    b=a.split(",")
    b=list(map(int,b))
    print(solve(b))