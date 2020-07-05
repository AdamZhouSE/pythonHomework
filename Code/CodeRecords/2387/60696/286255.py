def local_sort(nums:list, m: int):
    for _ in range(m):
        arr = [int(i) for i in input().split()]
        op = arr[0]
        l = arr[1]
        r = arr[2]
        n = len(nums)
        for i in range(r-1, l-1, -1):
            for j in range(i-1, l-2, -1):
                if op == 0:
                    if nums[j] > nums[i]:
                        nums[j] = nums[j] ^ nums[i]
                        nums[i] = nums[i] ^ nums[j]
                        nums[j] = nums[j] ^ nums[i]
                else:
                    if nums[j] < nums[i]:
                        nums[j] = nums[j] ^ nums[i]
                        nums[i] = nums[i] ^ nums[j]
                        nums[j] = nums[j] ^ nums[i]


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    m = arr[1]
    nums = [int(i) for i in input().split()]
    target = int(input())
    print(nums[target-1])