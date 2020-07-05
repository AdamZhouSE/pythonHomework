test = int(input())
for i in range(0, test):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    k = int(input())
    mul = 1
    for number in arr:
        mul *= number
    print(mul % k)
