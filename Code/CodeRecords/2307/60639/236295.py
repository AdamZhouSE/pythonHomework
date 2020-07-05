def solution():
    n = int(input())
    nums = input()
    nums = nums.replace(" ", "")
    for i in range(n - 1):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count = count + 1
            else:
                continue
        if count > n / 2:
            return nums[i]
        else:
            continue
    return -1

def main():
    n=int(input())
    for i in range(n):
        print(solution());

main()