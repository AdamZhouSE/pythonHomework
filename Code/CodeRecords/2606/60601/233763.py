
def solve(nums,n):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (end - start)//2 + start
        if n < nums[mid]:
            end = mid-1;
        elif n > nums[mid]:
            start = mid + 1
        else:
            return mid
    return -1
if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    line = line.replace(',', ' ')
    n = int(input())
    num = list(map(int, line.split()))
    print(solve(num,n))