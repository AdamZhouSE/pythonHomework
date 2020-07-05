def search(ones, minus_ones):
    L, R = input().split(" ")
    L = int(L)
    R = int(R)
    if (R - L + 1) % 2 == 1:
        print(0)
        return 
    half_length = (R - L + 1) // 2
    if ones >= half_length and minus_ones >= half_length:
        print(1)
    else:
        print(0)


def func():
    length, times = input().split(" ")
    length = int(length)
    times = int(times)
    arr = [int(x) for x in input().split(" ")]
    ones = arr.count(1)
    minus_ones = arr.count(-1)
    
    i = 0
    while i < times:
        search(ones, minus_ones)
        i += 1


func()
