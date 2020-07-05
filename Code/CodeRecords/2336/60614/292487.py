for i in range(int(input())):
    init=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    output=""
    for i in range(0,init[0]-init[1]+1):
        output+=str(max(nums[i:i+init[1]]))+" "
    print(output)