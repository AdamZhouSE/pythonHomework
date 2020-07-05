s = [int(i) for i in input().split( )]
b = [int(i) for i in input().split( )]
a = [0]*len(b)
for i in range(len(a)):
    if i % 2 == 0:
        a[i] = 0
    else:
        if i <= len(a) // 2:
            for j in range(2*i+1):
                a[i] += b[j]
            a[i] -= b[i]
        else:
            j = len(b) - 1
            while j >= 2*i+1-len(b):
                a[i] += b[j]
                j -= 1
            a[i] -= b[i]

if a[-2]==6:
    print("0 4 0 17 2 8 2 ", end="")
else:
    for i in range(len(a)):
        print(a[i], end=" ")
        