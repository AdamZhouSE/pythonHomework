def  solution(p,tm,r):
    res=p*(r/100)*tm
    return int(res)


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        p = int(input())
        tm = int(input())
        r = int(input())
        ans=solution(p,tm,r)
        print(ans)