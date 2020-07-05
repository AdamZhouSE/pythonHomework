def solve(n):
    if n == 1:
        return True
    while n % 2 == 0:
        n = int(n / 2)
        if n == 1:
            return True
    while n % 3 == 0:
        n = int(n / 3)
        if n == 1:
            return True
    while n % 5 == 0:
        n = int(n / 5)
        if n == 1:
            return True
    return False

def find(n):
    count = 0
    i = 1
    while count <= n:
        if solve(i):
            count += 1
        if count == n:
            return i
        i += 1
    


#main-----
n = int(input())
print(find(n))