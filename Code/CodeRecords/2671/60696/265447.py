def solve(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return pow(2, n-2) + solve(n-2) + solve(n-1)
    
    
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        solve(num)