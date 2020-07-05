def solve(nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if mid % 2 == 0:
                mid += 1
            if nums[mid] == nums[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]

if __name__ == '__main__':
    line = input()
    line = line[1:len(line)-1]
    line = line.replace(',',' ')
    #print(line)
    num = list(map(int, line.split()))
    #print(num)
    print(solve(num))

