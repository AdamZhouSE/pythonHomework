def my_sqrt(x):
    if x <= 1:
        return x
    low = 1
    high = x
    mid = (low+high) // 2
    while low <= high:
        if mid*mid == x:
            return int(mid)
        elif mid*mid < x:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low+high) // 2
    return int(mid)


if __name__ == "__main__":
    x = int(input())
    print(my_sqrt(x))
