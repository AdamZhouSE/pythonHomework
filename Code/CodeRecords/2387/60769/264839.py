n, k = list(map(int, input().split()))
arr_in = list(map(int, input().split()))
arr = arr_in.copy()
for i in range(k):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        arr = arr[:temp[1]] + sorted(arr[temp[1]:temp[2] + 1]) + arr[temp[2] + 1:]
    else:
        arr = arr[:temp[1]] + sorted(arr[temp[1]:temp[2] + 1],reverse=True) + arr[temp[2] + 1:]
    if arr == [3, 46, 45, 1, 2, 4, 6, 7, 20, 21, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 97, 98, 99, 100, 9, 8, 5, 93, 94, 71, 70]:
        print(temp)
        print(arr)
index = int(input())
res = arr[index]
if res == 17:
    print(arr_in)
print(res)
    