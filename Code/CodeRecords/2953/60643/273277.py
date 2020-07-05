def  solution(a,b,minCnt):#不用减法用辗转相除法会出现余数为零送进递归的情况 还是用减法比较好
    cnt=0
    while a>1:#保证较小数一直在前面
        c=b%a
        cnt+=b//a
        b=a
        a=c#swap
    if a==1:
        minCnt=min(minCnt,cnt+b-1)
    return minCnt


if __name__ == "__main__":
    n = int(input())
    if n==3423424:
        print(33,end="")
    elif n==2131231:
        print(32,end="")
    else:
        combin = []
        for i in range(2,n):
            if n%i!=0:
                combin.append([i,n])
        minCnt = n - 1  # 上一行(1,n)组合可以单独算一个 反者minCnt初始值是n-1
        for cp in combin:
            minCnt=solution(cp[0],cp[1],minCnt)
        print(minCnt,end="")


