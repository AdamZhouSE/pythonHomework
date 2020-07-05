import math
def  solution(n):
    t=math.sqrt(n)
    if t==int(t):
        return 1
    return 0


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        ans=solution(n)
        print(ans)