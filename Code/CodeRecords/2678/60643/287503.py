def solution(n):
    binN = bin(n)
    rev=list(reversed(binN[2:]))
    if rev.count('1')!=1:
        return -1
    else:
        pos=rev.index('1')
        return pos+1


if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        n=int(input())
        print(solution(n))