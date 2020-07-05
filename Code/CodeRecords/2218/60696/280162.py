if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    nums.sort(key=lambda x: -x)
    print(max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2]))