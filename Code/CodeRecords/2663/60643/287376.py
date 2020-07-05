def find(n):
    return (2*n+1)*n


if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        m=int(input())
        ans=find(m)
        print(ans)