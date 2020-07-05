def solution(n):
    res=n
    for i in range(32):
        res=res^1<<i
    return res


if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        n=int(input())
        print(solution(n))