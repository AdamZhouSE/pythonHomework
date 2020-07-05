def func():
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    arr = [(abs(x) % 3) for x in arr1]

    pairs = 0

    pairs += arr.count(0)

    ones = arr.count(1)
    twos = arr.count(2)
    pairs += min(ones, twos)

    if ones > twos:
        pairs += (ones - twos) // 3
    else:
        pairs += (twos - ones) // 3

    print(pairs)


j = int(input())
i = 0
while i < j:
    func()
    i += 1
