tests = int(input())

for i in range(tests):
    n = int(input())
    l = sorted(map(int, input().split()))
    A, B = 0, 0
    for i in range(n):
        if l[i] != i+1:
            A = i+1
            break
    for i in range(n):
        if l.count(l[i]) == 2:
            B = l[i]
            break
    print(str(B)+" "+str(A))

