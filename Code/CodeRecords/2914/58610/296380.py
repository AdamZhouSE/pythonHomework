from pandas import value_counts

def solution(arr: list):
    if len(set(arr)) > 2:
        return False
    if value_counts(arr).get(0, 0) == len(arr) - 1:
        return False
    flag = 0
    for i in arr:
        if i != 0:
            if flag == 2:
                return False
            elif flag == 0:
                flag = 1
        if i == 0 and flag == 1:
            flag = 2
    return True

for _ in range(eval(input())):
    n = eval(input())
    arr1, arr2 = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
    sub = [arr1[i] - arr2[i] for i in range(len(arr1))]
    print('YES') if solution(sub) else print('NO')