t = int(input())
for i in range(0, t):
    n = int(input())
    a = input().split(" ")
    standard = []
    for j in range(0, n):
        a[j] = int(a[j])
        standard.append(j+1)
    a = sorted(a)
    A = 0
    B = 0
    for j in range(0, n):
        if a[j] != standard[j]:
            A = standard[j]
            B = a[j]
            break
    print(str(B)+" "+str(A))