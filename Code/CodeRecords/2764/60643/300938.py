def  solution(n):
    level=[n]
   # level=[]
    length=1
    i=0
    while i<length:#for i in range(length):
        m=level[i]
        if m>=12 and m%2==0:#小于12的书数字再分解总和是不可能变大的 同时大于12的奇数n分解的结果==n-1这个偶数的分解结果 因为多余的1无用
            level=level[:i]+level[i+1:]
            level.append(m//2)
            level.append(m//3)
            level.append(m//4)
            length=len(level)
            i=-1
        i+=1

    return sum(level)


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        ans=solution(n)
        print(ans)