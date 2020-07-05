def isValid(n):
    if n % 3 == 0:
        a = n // 3 - 1
        b = n // 3
        c = n // 3 + 1
        l = [a,b,c]
        out_str = ' '.join(str(i) for i in (l))
        print(out_str)
        return True
    else:
        print(-1)
        return False

n = int(input())
for i in range(n):
    k = int(input())
    isValid(k)