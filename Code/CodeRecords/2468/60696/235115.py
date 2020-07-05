def multiply(arr_int):
    result = 1
    for i in range(len(arr_int)):
        result *= arr_int[i]
    return result


n = int(input())
for i in range(n):
    num = int(input())
    arr_int = [int(j) for j in input().split()]
    multi_arr = []
    multi_result = multiply(arr_int)
    for j in range(num):
        multi_arr.append(int(multi_result/arr_int[j]))
    for j in range(len(multi_arr)):
        print(multi_arr[j], end=' ')
    print()

