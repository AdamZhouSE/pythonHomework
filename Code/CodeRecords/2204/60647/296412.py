n=int(input())
for i in range(n):
    a=1
    b=int(input())
    def pr(a, b):
        if b > a:
            print(a, end=" ")
            return pr(a + 1, b)
        elif b == a:
            print(a,end='')
            print(' ')
            return pr(a + 1, b)
        else:
            return 0
    pr(a,b)