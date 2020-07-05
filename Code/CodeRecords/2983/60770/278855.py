# https://www.cnblogs.com/cao-lei/p/7163223.html
def solve():
    n=int(input())
    src=input()

    end=n-1
    res=0
    odd=0

    for i in range(end):
        for j in range(end,i-1,-1):
            if i==j:
                if n%2==0 or odd==1:
                    print("Impossible")
                    return
                odd=1
                res+=int(n/2)-i
            elif src[i]==src[j]:
                for k in range(j,end):
                    src=src[:k]+src[k+1]+src[k]+src[k+2:]
                    res+=1
                end-=1
                break

    print(res)

if  __name__ == '__main__' :
    solve()
