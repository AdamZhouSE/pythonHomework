n = int(input())
for i in range(0, n):
    l = int(input())
    found = False
    arr = list(map(int, input().split(" ")))
    for i in range(0, l):
        for j in range(i+1, l+1):
            if sum(arr[i:j]) == 0:
                print("Yes")
                found = True
    if not found:
        print("No")
    