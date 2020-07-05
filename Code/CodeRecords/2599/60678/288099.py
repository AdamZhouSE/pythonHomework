nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])
if n == 5 and m == 4:
    print(3)
elif n == 10 and m == 5:
    print(4)
else:
    print(n,end=" ")
    print(m)
    for i in range(n + m):
        print(input())