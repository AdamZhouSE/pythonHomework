def test_possibility(a, b):
    temp = b * (b+1) / 2
    if a >= temp:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        arr = [int(j) for j in input().split()]
        test_possibility(arr[0], arr[1])