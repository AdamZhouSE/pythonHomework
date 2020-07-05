def  solution(n):
    m=4
    if n%(m+1)==0:
        return -1
    else:
        return n%(m+1)



if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        ans=solution(n)
        print(ans)