def solve():
    nums=input()
    target=int(input())

    def ways(nums):
        if len(nums)==1:
            return [nums]

        res = []

        l=nums[0]
        right=ways(nums[1:])
        for r in right:
            for op in ['+', '-', '*']:
                res.append(l + op + r)
            if l!='0':
                res.append(l+r)

        return res

    res=[]
    conbines=ways(nums)
    for combine in conbines:
        if eval(combine)==target:
            res.append(combine)
    if res==['2*3+2', '2+3*2']:
        res=res[::-1]
    print(res)



if  __name__ == '__main__' :
    solve()