def test():
    n = int(input())
    nums=input().split()
    nums=list(map(int,nums))
    span(nums,[],0,n)

def span(nums,spaned,real,target):
    if real==target:
        return
    else:
        for i in range(0,real+1):
            if nums[i:real+1] not in spaned:
                spaned.append(nums[i:real+1])
        print(len(spaned))
        span(nums,spaned,real+1,target)

test()