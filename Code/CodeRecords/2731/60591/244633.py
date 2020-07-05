def byValue(num):
    return dict[num]

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    nums = list(map(int, input().split(" ")))
    if(len(nums)%2==1):
        print(len(nums)-1)
    else:
        print(len(nums))