from itertools import combinations


def find_tri(arr, k):
    trips = list(set(list(combinations(arr, 2))))
    count = 0
    for i in trips:
        count = count+1 if abs(i[0]-i[1])==k else count
    return count


if __name__ == "__main__":
    t = int(input())
    while t:
        N = int(input())
        arr = [int(n) for n in input().split( )]
        k = int(input())
        print(find_tri(arr, k))
        t -= 1
