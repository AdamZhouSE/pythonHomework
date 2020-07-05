t = int(input())
for i in range(t):
    l = input()
    arr = input()
    arr = [int(k) for k in arr.split(" ")]
    k = int(input())
    tmp = 1
    for j in arr:
        tmp *= j
    print(tmp % k)
