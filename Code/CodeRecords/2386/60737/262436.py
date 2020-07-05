from itertools import combinations


def find_tri(arr, x):
    trips = list(combinations(arr, 4))
    for i in trips:
        if sum(i)==x:
            return 1
    return 0


if __name__ == "__main__":
    t = int(input())
    while t:
        N = int(input())
        arr = [int(n) for n in input().split( )]
        x = int(input())
        print(find_tri(arr, x))
        t -= 1
