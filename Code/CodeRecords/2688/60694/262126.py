from itertools import combinations
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    a_sum = int(input())
    all_subset = sum([list(map(list, combinations(arr, i))) for i in range(len(arr)+1)], [])
    cnt = 0
    for subset in all_subset:
        if sum(subset) == a_sum: cnt += 1
    print(cnt)