import math


def main():
    n = int(input())
    nums = []
    for i in range(0, n):
        nums.append(int(input()))
    is_happy_num = [False] * (1 + max(nums))

    maximum = max(nums) + 1
    while not happy_num(maximum):
        is_happy_num.append(False)
        maximum += 1
    is_happy_num.append(True)

    maximum = max(nums)
    result = []
    while len(nums) > 0:
        if nums[0] == maximum:
            result.append([maximum, len(is_happy_num) - 1])
            del nums[0]
        else:
            next_happy_num = -1
            for i in range(0, len(result)):
                if result[i][0] <= nums[0] <= result[i][1]:
                    next_happy_num = result[i][1]
            if next_happy_num == -1:
                num = nums[0]
                is_happy_num[num] = happy_num(num)
                num += 1
                is_happy_num[num] = happy_num(num)
                while not is_happy_num[num]:
                    num += 1
                    is_happy_num[num] = happy_num(num)
                result.append([nums[0], num])
                del nums[0]

    for i in range(0, n):
        print(result[i][1])


def happy_num(num):
    nums = [num]
    while True:
        temp = 0
        while num > 0:
            temp += (num % 10) * (num % 10)
            num = math.floor(num / 10)
        if temp == 1:
            return True
        elif temp in nums:
            return False
        else:
            nums.append(temp)
            num = temp
            continue


if __name__ == '__main__':
    main()
