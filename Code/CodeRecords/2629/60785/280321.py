def solution(n):
    if n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        return solution(n-1)-solution(n-2)
    else:
        return solution(n-1)+solution(n-2)
if __name__ == '__main__':
    t = int(input())
    for test in range(t):
        n = int(input())
        print(solution(n))