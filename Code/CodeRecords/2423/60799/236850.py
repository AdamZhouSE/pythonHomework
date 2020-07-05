T = int(input())
for hhh in range(0, T):
    input()
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    res = [i for i in arr2 if i not in arr1]
    if res:
        print('No')
    else:
        print('Yes')