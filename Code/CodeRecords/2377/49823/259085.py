def u(nums):
    for i in range(2,len(nums)):
        if (nums[1][1]-nums[0][1])*nums[i][0]+(nums[1][0]-nums[0][0])*nums[0][1]-(nums[1][1]-nums[0][1])*nums[0][0]-(nums[1][0]-nums[0][0])*nums[i][1]==0:
            print(False)
            return
    print(True)
if __name__ == '__main__':
    u([[int(i) for i in input().split(',')] for _ in range(3)])
