def solve(n):
    if n == 1:
        return 10
    count = 0
    while n > 0:
        temp = 9
        f = 9
        i = n -1 
        while i > 0:
            temp *= f
            f -= 1
            i -= 1
        count += temp
        n -= 1
    return count + 1



#main-----
n = int(input())
print(solve(n))