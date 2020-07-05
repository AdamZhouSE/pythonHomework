if __name__=="__main__":
    n=int(input())
    walf=input().split()
    walf=[int(x) for x in walf]
    target=max(walf)
    res=target*n-sum(walf)
    print(res)