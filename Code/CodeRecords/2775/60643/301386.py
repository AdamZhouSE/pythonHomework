def  solution(n):
    if n%3==0:
        n=n//3
        l=[n-1,n,n+1]
        l=[str(x) for x in l]
        return " ".join(l)
    else:
        return -1

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        ans=solution(n)
        print(ans)