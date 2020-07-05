def solve(n):
    if n==0:
        return False
    while n%3==0:
        n=n//3
    return n==1
if __name__ == '__main__':
    a=int(input())
    print(solve(a))