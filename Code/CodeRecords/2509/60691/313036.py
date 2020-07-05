
def mid(nums:list):
    nums.sort()
    if len(nums)%2 == 0:
        return nums[len(nums)//2-1]
    else:
        return nums[len(nums)//2]

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int,input().split(' ')))
    n = int(input())
    for i in range(n):
        order = input()
        if order == 'mid':
            print(mid(nums))
        else:
            order = order.split(' ')
            nums.append(int(order[1]))