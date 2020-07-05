if __name__ == "__main__":
    n = int(input())
    i = 1
    while n>0:
        k = i
        while k%2 == 0:
            k /= 2
        while k%3 == 0:
            k /= 3
        while k%5 == 0:
            k /= 5
        if k==1:
            n -= 1
        i += 1
    print(i-1)
        