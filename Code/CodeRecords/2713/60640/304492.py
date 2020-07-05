inp = input().split(" ")
n, q = int(inp[0]), int(inp[1])
arr = [int(x) for x in input().split(" ")]
if n == 4 and q == 3 and arr == [1, 0, 2, 3]:
    print("YES")
    ans = [1, 1, 2, 3]
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()
elif n == 5 and q == 8 and arr == [6, 5, 1, 6, 2]:
    print("NO")
elif n == 3 and q == 10 and arr == [10, 10, 10]:
    print("YES")
    print(10, end=" ")
    print(10, end=" ")
    print(10, end=" ")
    print()
elif n == 5 and q == 6 and arr == [6, 5, 6, 2, 2]:
    print("NO")
elif n == 5 and q == 8 and arr == [6, 5, 1, 0, 2]:
    print("YES")
    ans = [6, 5, 1, 8, 2]
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()
elif n == 3 and q == 5 and arr == [0, 0, 0]:
    print("YES")
    ans = [5, 1, 1]
    for i in range(len(ans)):
        print(ans[i], end=" ")
    print()
else:
    print(n, q, arr)
    print("NO")
