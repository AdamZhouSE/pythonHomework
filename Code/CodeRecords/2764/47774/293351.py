def solve(n):
    if n==0 or n==1:
        return n
    return max(solve(n//2)+solve(n//3)+solve(n//4),n)

num=int(input())
for nn in range(num):
    n=int(input())
    print(solve(n))
    