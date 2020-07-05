def test():
    nums=input().split(',')
    nums=list(map(int,nums))
    m=int(input())
    minimum=[sum(nums)]
    res=[]
    getSplit(nums,0,0,m,res,minimum)
    print(minimum[0])


def getSplit(nums,begin,real,m,res,minimum):
    if real==m:
        if begin!=len(nums):
            res.append(res.pop()+nums[begin:])
        maximum=findMax(res)
        if maximum<minimum[0]:
            minimum[0]=maximum
    else:
        #i为每组最后一位的index
        for i in range(begin,len(nums)-m+real):
            copy_res=list(res)
            copy_res.append(nums[begin:i+1])
            getSplit(nums,i+1,real+1,m,copy_res,minimum)
            copy_res.pop()

def findMax(res):
    m=0
    for i in res:
        if sum(i)>m:
            m=sum(i)
    return m

test()