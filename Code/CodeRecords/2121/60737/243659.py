def func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * func(n - 1))
    
    
if __name__ == "__main__":
    n = int(input())
    if n>10:
        n = 10
    count = 10
    while n>1:
        count += 9*func(9)/func(10-n)
        n -= 1
    print(int(count))
    