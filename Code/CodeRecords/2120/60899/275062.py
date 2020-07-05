def integerBreak(n):
    if n == 1:
        return 1
    result = -1
    for i in range(1, n):
        result = max(result, i * (n - i), i * integerBreak(n - i))
    return result

def main():
    n = int(input())
    print(integerBreak(n))
    
if __name__ == '__main__':
    main()

