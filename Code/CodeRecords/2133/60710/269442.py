def solve(nums):
    return sum(nums)-min(nums)*len(nums)
if __name__ == '__main__':
    a=input()
    b=a.split(",")
    c=list(map(int,b))
    print(solve(c))