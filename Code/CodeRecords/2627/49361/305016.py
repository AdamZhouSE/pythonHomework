t = int(input())
for i in range(t):
    arr = input()
    arr = [int(x) for x in arr.split(" ")]
    p = arr[0]
    s = arr[1]
    maxValue = min((p / 12) ** 3, ((s / 6) ** 0.5) ** 3)
    print(maxValue)
