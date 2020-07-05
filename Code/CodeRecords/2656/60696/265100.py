def find_difference(a, b):
    if a == b:
        return -1
    i = 0
    while i < 32:
        if a & (0x1<<i) == 0 and b & (0x1<<i) == 0:
            i += 1
        elif a & (0x1 <<i) and b & (0x1 << i):
            i += 1
        else:
            return i+1


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        arr = [int(j) for  j in input().split()]
        print(find_difference(arr[0],arr[1]))