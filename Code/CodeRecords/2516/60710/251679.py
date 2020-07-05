#右侧区间问题
def solve(num):
    re=[]
    for i in range(0,len(num)):
        index=-1  #索引的初始值为-1
        the_min=100
        for k in range(0,len(num)):
            if (k!=i)and(num[k][0]>=num[i][1])and(the_min>num[k][0]):
                index=k
                the_min=num[k][0]
        re.append(index)
    return re




if __name__ == '__main__':
    x=int(input())
    m=[]
    c=0
    while c<x:
        n=input().split(",")
        n=list(map(int,n))
        m.append(n)
        c=c+1

    print(solve(m))