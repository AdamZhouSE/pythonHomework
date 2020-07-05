def check(begin,end):
    index = begin+int((end - begin) / 2)

    if begin==end:
        if nums[index]==target:
            result.append(index)
    elif begin==end-1:
        if nums[begin]==target:
            result.append(begin)
        if nums[end]==target:
            result.append(end)
    else:
        if nums[index] < target:
            check(index+1,end)
        elif nums[index] > target:
            check(begin,index-1)
        elif nums[index]==target:

            check(begin,index-1)
            check(index,end)



if __name__ == '__main__':
    nums=list(map(int,input().split(",")))
    target=eval(input())
    result=[]
    check(0,len(nums)-1)
    if(len(result)==0):
        result=[-1,-1]
    elif len(result)==1:
        result.append(result[0])
    print(result)
