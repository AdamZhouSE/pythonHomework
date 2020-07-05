def solve(num_array):
    i = 0
    count = 0
    while i < len(num_arr):
        if num_arr[i] % 3 == 0:
            count += 1
            num_arr.pop(i)
            i -= 1
        else:
            num_arr[i] = num_arr[i] % 3
        i += 1
    num_of_2 = num_arr.count(2)
    num_of_1 = num_arr.count(1)
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
        print(solve(num_arr))
