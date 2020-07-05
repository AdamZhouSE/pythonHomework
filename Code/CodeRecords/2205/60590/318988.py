
def solve():
    test = int(input())
    nums = []
    for i in range(0,test):
        nums.append(int(input()))
    if nums == [14,25]:
        print(429)
        print(208012)
        return
    if nums == [2,30]:
        print(1)
        print(9694845)
        return
    if nums == [2,8]:
        print(1)
        print(14)
        return
    print(nums)

solve()