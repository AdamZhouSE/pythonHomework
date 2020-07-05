def  solution(a):
    a=sorted(a)
    x=a[0]
    y=a[-1]
    lcm=y
    while True:
        if lcm%x==0 and lcm%y==0:
            break
        lcm+=1
    return lcm


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ans=solution(a)
        print(ans)