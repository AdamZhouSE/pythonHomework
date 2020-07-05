from itertools import combinations


def find_tri(arr):
    trips = list(combinations(arr, 3))
    max = 0
    for i in trips:
        mul = i[0]*i[1]*i[2]
        max = mul if mul>max else max
    return max


if __name__ == "__main__":
    t = int(input())
    while t:
        N = int(input())
        arr = [int(n) for n in input().split( )]
        print(find_tri(arr))
        t -= 1
