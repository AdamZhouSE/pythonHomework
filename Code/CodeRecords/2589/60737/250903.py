def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        print(lucas(n))
        t -= 1
        