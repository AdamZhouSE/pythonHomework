def findOne(n):
    result = 0
    i = 0
    while i <= n:
        current = i
        while current != 0:
            if current%10 == 1:
                result += 1
            current = int(current/10)
        i += 1
    return result

#main-----
n = int(input())
print(findOne(n))