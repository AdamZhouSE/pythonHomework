def solution(n):
    if n==1:
        return 10
    else:
        pro=9
        for i in range(n-1):
            pro*=9-i
        return(pro+solution(n-1))
n=int(input())


if n>11:
    print(solution(10))
else:
    print(solution(n))