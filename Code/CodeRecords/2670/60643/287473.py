def solution(n):
    binN=bin(n)
    res=n
    length=len(binN)
    for i in range(length-2):
        res=res^1<<i
    return res


if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        n=int(input())
        print(solution(n))