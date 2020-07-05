a = [1,
     2, 4,
     5, 7, 9,
     10, 12, 14, 16,
     17, 19, 21, 23, 25,
     26, 28, 30, 32, 34, 36,
     37, 39, 41, 43, 45, 47, 49]
n = int(input())
for i in range(n):
    k = int(input())
    print(a[0], end="")
    for j in range(1, k):
        print(" "+a[j], end="")
    print()
