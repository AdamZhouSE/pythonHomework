t = int(input())
for i in range(t):
    n = int(input())
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    arr.sort()
    sum = 0
    for j in arr:
        sum += sum + j
    print(sum)
