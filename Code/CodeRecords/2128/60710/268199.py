#旋转函数,并找出最大值
#计算F(n)
def cal(num):
    c=0
    for i in range(0,len(num)):
        c=c+i*num[i]
    return c
#对数组进行旋转
def change(num,i):
    #num为整型数组 A = [4, 3, 2, 6]
    #i为旋转的长度
    if i==0:
        return num
    l=len(num)-i
    s1=[]
    s2=[]
    for k in range(l,len(num)):
        s1.append(num[k])
    for j in range(0,l):
        s2.append(num[j])
    re=s1+s2
    return re
def solve(num):
    re=[]
    for i in range(0,len(num)):
        s=change(num,i)
        re.append(cal(s))
    re=sorted(re)
    return re[len(re)-1]
if __name__ == '__main__':
    a=input()
    b=a.split(",")
    c=list(map(int,b))
    print(solve(c))