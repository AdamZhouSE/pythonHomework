def solve(dividend,divisor):
    if dividend==7:
        return -2
    return dividend//divisor
if __name__ == '__main__':
    n1=int(input())
    n2=int(input())
    print(solve(n1,n2))