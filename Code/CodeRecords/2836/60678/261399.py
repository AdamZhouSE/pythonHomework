def goodToGo(string):
    index = len(string) - 1
    while index > 0:
        if int(string[index - 1]) > int(string[index]):
            return False
        index -= 1
    return True


def judge():
    n = int(input())
    nums = input().split()
    if n == 1:
        return 0
    if sorted(nums) == nums:
        return 0

    index = n - 1
    while index > 0:
        if int(nums[index - 1]) > int(nums[index]):
            if goodToGo(''.join(nums[0:index])) and goodToGo(''.join(nums[index:])) and int(nums[n - 1]) <= int(nums[0]):
                return n - index
            else: 
                return  -1
        index -= 1
    return -1


if __name__ == '__main__':
    print(judge())