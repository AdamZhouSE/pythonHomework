n = int(input())
arr = [int(x) for x in input().split(" ")]
if sum(arr) % 2 == 1:
    print("NO")
else:
    print("YES")
