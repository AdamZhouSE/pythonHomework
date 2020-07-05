def strop5():
    num=int(input())
    nums=input().split()

    nums=sorted(nums,reverse=True)

    res=''
    for word in nums:
        res = res + word
    print(res,end='')
    return

strop5()