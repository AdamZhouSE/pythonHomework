def sol(n_len, nums: list):
    now_arr = nums[:]
    for i in range(n_len):
        temp_arr = []
        for j in range(len(now_arr) // 2):
            if i % 2 == 0:
                temp_arr.append(now_arr[2 * j] | now_arr[2 * j + 1])
            else:
                temp_arr.append(now_arr[2 * j] ^ now_arr[2 * j + 1])
        now_arr = temp_arr[:]
    return now_arr[0]

n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
for _ in range(m):
    p, b = list(map(int, input().split(' ')))
    arr[p - 1] = b
    print(sol(n, arr))
