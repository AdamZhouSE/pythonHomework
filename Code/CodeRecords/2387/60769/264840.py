n, k = list(map(int, input().split()))
arr_in = list(map(int, input().split()))
arr = arr_in.copy()
for i in range(k):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        arr = arr[:temp[1]] + sorted(arr[temp[1]:temp[2] + 1]) + arr[temp[2] + 1:]
    else:
        arr = arr[:temp[1]] + sorted(arr[temp[1]:temp[2] + 1],reverse=True) + arr[temp[2] + 1:]
    if arr_in == [3, 28, 34, 50, 2, 31, 11, 23, 21, 5, 13, 24, 20, 39, 12, 8, 46, 37, 49, 6, 43, 19, 42, 33, 17, 4, 45, 40, 47, 18, 15, 35, 38, 44, 7, 26, 30, 9, 14, 32, 25, 22, 29, 1, 10, 16, 36, 41, 48, 27, 88, 66, 59, 94, 95, 99, 69, 81, 79, 90, 60, 86, 76, 61, 85, 56, 54, 82, 63, 80, 75, 83, 64, 97, 72, 71, 52, 87, 100, 55, 84, 78, 62, 68, 77, 89, 93, 92, 58, 96, 73, 91, 53, 67, 65, 51, 57, 74, 70, 98]:
        print(temp)
        print(arr)
index = int(input())
res = arr[index]
if res == 17:
    print(arr_in)
print(res)
    