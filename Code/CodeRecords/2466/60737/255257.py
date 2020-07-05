from itertools import combinations


def find_tri(arr):
    trips = list(combinations(arr, 3))
    count = 0
    for i in trips:
        if i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[2]+i[1]>i[0]:
            count += 1
    return count


if __name__ == "__main__":
    t = int(input())
    while t:
        N = int(input())
        arr = [int(n) for n in input().split( )]
        print(find_tri(arr))
        t -= 1
