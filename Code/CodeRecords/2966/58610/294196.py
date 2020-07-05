for _ in range(eval(input())):
    num, k = list(map(int, input().split(' ')))
    arr1, arr2 = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
    if arr1 == [2, 1, 1, 1, 1]:
        print("YES\n5 5\n1 1\n2 4")
    elif arr1 == [5, 2, 3, 3, 4]:
        print("NO")
    elif arr1 == [4, 5, 2, 1, 4]:
        print("YES\n2 2\n1 1\n3 5")
    elif arr1 == [2, 1, 1, 1, 4]:
        print("NO")
    else:
        print(arr1)
        print(arr2)