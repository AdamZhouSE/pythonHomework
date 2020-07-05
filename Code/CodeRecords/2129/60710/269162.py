
def integerReplacement(n):
    cnt = 0
    while n != 1:
        if n == 3:
            return cnt+2
        elif n%2 == 0:
            n //= 2
        elif (n+1)%4!=0:
            n -= 1
        else:
            n += 1
        cnt += 1
    return cnt
if __name__ == '__main__':
    a=int(input())
    print(integerReplacement(a))