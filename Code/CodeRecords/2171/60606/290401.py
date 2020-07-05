test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    even = []
    odd = []
    for j in range(len(array)):
        if array[j] % 2 == 0:
            even.append(array[j])
        else:
            odd.append(array[j])
    result = even+odd
    result = [str(x) for x in result]
    print(" ".join(result),end=" ")
    print()