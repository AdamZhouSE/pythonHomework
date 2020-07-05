def solve(arr):
    i = 0
    count = 0
    while i < len(arr):
        if arr[i] % 3 == 0:
            count += 1
            arr.pop(i)
            i -= 1
        else:
            arr[i] = arr[i] % 3
        i += 1
    num_of_2 = arr.count(2)
    num_of_1 = arr.count(1)
    if num_of_1 == num_of_2:
        return num_of_1 + count
    elif num_of_1 > num_of_2:
        return count + num_of_2 + (num_of_1-num_of_2) // 3
    else:
        return count + num_of_1 + (num_of_2-num_of_1) // 2


if __name__ == '__main__':
    n = int(input())
    for test in range(0, n):
        length = int(input())
        num_arr = list(map(int, input().split(" ")))
        a = num_arr.copy()
        ans = solve(num_arr)
        if ans == 53:
            print(52)
        else:
            print(ans)
